# Deploy.pi
## Get Accounts Functionality
Devuelve la address de mi account segun como este asignada en el file config.yaml, utiliza el methodo accounts:
from brownie import accounts

**def deploy_token_farm_and_att_token():**
Cuando llamo el parametro TokenFarm (del contrato.sol) y el comando deploy, estoy llamando al constructor dentro del contrato, y necesito darle los parametros definidos, en este caso:

    constructor(address _aaTokenAddress) public {
        aaToken = IERC20(_aaTokenAddress);

el aaTokenAddress.

Ahora parece que la sigueinte transaccion envia todo el dinero a la granja, eso es buena idea?? no deberian guardarse cierta cantidad de fondos reservados por las dudas.

The fake tokens, mocks, are cheated contracts used to deploy locally when testing. 

Thats what the function get_contract is for...
fau_token = get_contract("fau_token")
The string "fau_token" needs to match the string in the config.yaml file exactly ....fau_token: "0xFab46E

At this staged I had to copy the whole folder contract/test from the chainlink mix repo into the contracts folder...

After that necesitamos mock correctamente el weth y el fau tokens...

** MockDAI **
Esto es para el FAU token
Recordar que los sol primero llamo contract, y luego el constructor...
