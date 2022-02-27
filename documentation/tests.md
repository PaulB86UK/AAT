# Test set price feed contract 
network.show_active() to show the current network. LOCAL_BLOCKCHAIN_ENVIRONMENTS es una variable definida en pp_tools, se pueden importar variables de un codigo python a otro.

Este test lo que hace es verificar que el price obtenidi por la funcion get contract eth_usd price feed iguala el precio asignado al aat token, usando la funcion setpricefeedcontract en el token farmm contract.  

# The second test verifies that non owners cant call the function with their accounts which is not the owners

Apparently the idea is to check every function in the contract TokenFarm Sol and test them. The above one tested was

    function setPriceFeedContract(address _token, address _priceFeed)
        public
        onlyOwner
    {
        tokenPriceFeedMapping[_token] = _priceFeed;
    }

Its unit testing since its doing functions by functions. 

First before the issue tokens we need to have tokens staked. Yes because issue tokens is the reward. A nice functionality was used where a conftest.py with a fixture was created, and apparently the variable gets automatically migrated into the test python file as amount_staked.
So the test here is to stake a defined amount of tokens using the script, and then check in the contract the right amount of tokens have been staked.

A look up in the functionality, here we are using the stakingBalance parameter which is a mapping. Like this:
mapping(address => mapping(address => uint256)) public stakingBalance;

It has two address on it, the token address which is also mapped to a acount addres, so when calling this mapping the following sintax is needed:

token_farm.stakingBalance(aat_token.address,account.address)

Where you call each portion of the mapping as independent parameters listed by commas on the function.

So again this shall return the balance on the account which will match the staked amount variable if the code worked as expected/

The web3 error is common in brownie and a known bug, time.sleep is needed at the end of code or tx.wait(1) in oder to avoid it.

Also the stakeTokens method activates the updateUniqueTokensStaked method, that addes the token to the list if the user dont have it. And the second assert test this work ok.

assert token_farm.uniqueTokensStaked(account.address) == 1

lastly the function do stakers.push so we need to check if we are also in the list of stakers as a final test of the function

assert token_farm.stakers(0) == account.address

Finally we perform return token_farm, aat_token so we can use the variables of this test into another test


# The next function is **issue tokens**

## def test_issue_tokens():

Again this works for the rewards of people staking tokens. We use the previous test, as this one builds on top of the previous, where in order to give rewards, we need tokens staked///

so first we check the initial staking balance, then apply the rewards, and the difference should match the number expected???


