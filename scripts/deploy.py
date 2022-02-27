from .pp_functions import get_account, get_contract
from brownie import AAToken, TokenFarm, config, network

# PARAMETERS
KEPT_BALANCE = 2780400000000000000000000000 * 0.51  # keep 51% of the tokens


def main():
    deploy_token_farm_and_att_token()


def deploy_token_farm_and_att_token():
    account = get_account()
    aat_token = AAToken.deploy({"from": account})
    token_farm = TokenFarm.deploy(
        aat_token.address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    tx = aat_token.transfer(
        token_farm.address,
        aat_token.totalSupply() - KEPT_BALANCE,
        {"from": account},
    )
    tx.wait(1)
    # 3 tokens: aat token, weth_token, fau_token(is DAI?)
    weth_token = get_contract("weth_token")
    fau_token = get_contract("fau_token")
    dict_of_allowed_tokens = {
        aat_token: get_contract("dai_usd_price_feed"),
        fau_token: get_contract("dai_usd_price_feed"),
        weth_token: get_contract("eth_usd_price_feed"),
    }
    add_allowed_tokens(token_farm, dict_of_allowed_tokens, account)
    return token_farm, aat_token


def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):
    for token in dict_of_allowed_tokens:
        add_tx = token_farm.addAllowedTokens(token.address, {"from": account})
        add_tx.wait(1)
        set_tx = token_farm.setPriceFeedContract(
            token.address, dict_of_allowed_tokens[token], {"from": account}
        )
        set_tx.wait(1)
    return token_farm
