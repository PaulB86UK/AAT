# Funcion TokenIsAllowed  & function addAllowedTokens
Cerifica si el token se puede stakear vs una lista allowedTokens, tambien otra funcion addAllowedTokens permite agregar, (O sacar) tokens de la lista.
After checking si el token elegido se puede stakear/desestakear, ahora para hacerlo esto requiere transferir un token de una billetera a la otra, y quizas guardarlo en otra forma, como sAAT, que es el token stakeado?

# function stakeTokens

## Transfer From

### Codigo 
**function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)**

### Notas
* msg.sender es el que quiere stakear, el que tiene que depositar los fondos a nuestra direccion donde seran stakeados.
* adress(this) es la direccion de este contrato TokenFarm
* Ahora una ves transferidos necesitamos saber la cantidad transferida de cada persona, entonces hay que hacer un mapping que asigne la cantidad stakeada a una direccion particular. token address -> staker address -> amount. **Los mapping (TODOS) van al principio..**

maping token address -> staker address -> amount
mapping(address => mapping(address => uint256)

El balance staking del token _token por la persona msg.sender es igual a la cantidad que tenian originalmente mas la cantidad _amount transferida:

stakingBalance[_token][msg.sender] = stakingBalance[_token][msg.sender] + _amount

### Definicion 


Transfers _value amount of tokens from address _from to address _to, and MUST fire the Transfer event.


The transferFrom method is used for a withdraw workflow, allowing contracts to transfer tokens on your behalf. This can be used for example to allow a contract to transfer tokens on your behalf and/or to charge fees in sub-currencies. The function SHOULD throw unless the _from account has deliberately authorized the sender of the message via some mechanism.
Note Transfers of 0 values MUST be treated as normal transfers and fire the Transfer event.

# function IssueTokens
Reward of people that use the site and the staking.

address[] public stakers; List of all stakers of the platform

# function updateUniqueTokensStaked
Give an idea how many different tokens an user has. if the user has at least 1 token no need to add to the list, if not must do, also remove if he get all out

its an internal function only this contract can call this function!!! why the others are public then??

Entonces se fija en el stakingbalance si para ese token el usuario tiene algo stakeado, y sino agrega +1 en la lista uniquetokenStaked para ese usuario
los mappings, se llaman con corchete como si fueran diccionarios 
Ejemplo el mapping staking balance es:
mapping(address => mapping(address => uint256)) 
Entonces se llama de la siguiente manera
StakingBalance[_token address][_user address] y devuelve la cantidad

        if (uniqueTokensStaked[msg.sender] == 1){
            stakers.push(msg.sender);
        }
Nunca puede ser 0 por que al momento que se completo la transferencia pasa a ser 1, y si es mayor de 1 ya esta en la lista :)


# getUserTotalValue(recipient);
Esta funcion va a determinar la cantidad de recompensas que debe recibir el usuario por tener plata stakeada.

Patrick menciona que la forma en que esta hecho aca no es la mas eficiente, y que consume mucho gas el loop, es mas rapido si el usuario elige, habria que ver eso en mas detalle,

# getTokenValue
tokenPriceFeedMapping to associate the address of a token with the current price

#    function setPriceFeedContract(address _token, address _priceFeed)
    public
    onlyOwner {
        tokenPriceFeedMapping[_token] = priceFeed;
    }
This allows the owner of the contract to assign a pricefeed to a particular token
