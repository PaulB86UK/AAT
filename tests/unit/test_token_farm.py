from asyncio import exceptions
from brownie import network, exceptions
from scripts.pp_functions import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    INITIAL_PRICE_FEED_VALUE,
    get_account,
    get_contract,
)
import pytest
from scripts.deploy import deploy_token_farm_and_att_token
import time


def test_set_price_feed_contract():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")
    account = get_account()
    non_owner = get_account(index=1)
    price_feed_address = get_contract("eth_usd_price_feed")
    token_farm, aat_token = deploy_token_farm_and_att_token()
    # Act
    token_farm.setPriceFeedContract(
        aat_token.address, price_feed_address, {"from": account}
    )
    # Assert
    assert token_farm.tokenPriceFeedMapping(aat_token.address) == price_feed_address
    with pytest.raises(exceptions.VirtualMachineError):
        token_farm.setPriceFeedContract(
            aat_token.address, price_feed_address, {"from": non_owner}
        )


def test_stake_tokens(amount_staked):
    # Arrange
    ##local network testing
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")
    account = get_account()
    token_farm, aat_token = deploy_token_farm_and_att_token()

    # Act
    aat_token.approve(token_farm.address, amount_staked, {"from": account})
    token_farm.stakeTokens(amount_staked, aat_token.address, {"from": account})

    # Assert

    assert (
        token_farm.stakingBalance(aat_token.address, account.address) == amount_staked
    )
    time.sleep(1)

    assert token_farm.uniqueTokensStaked(account.address) == 1
    assert token_farm.stakers(0) == account.address

    return token_farm, aat_token


def test_issue_tokens(amount_staked):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")
    account = get_account()
    # bring the environment of the last test.
    token_farm, aat_token = test_stake_tokens(amount_staked)
    starting_balance = aat_token.balanceOf(account.address)

    # Act
    token_farm.issueTokens({"from": account})
    # Arrange
    assert (
        aat_token.balanceOf(account.address)
        == starting_balance + INITIAL_PRICE_FEED_VALUE
    )
