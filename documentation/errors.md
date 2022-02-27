
**En este error me olvide de definir el tipo de la variable _token**


DeclarationError: Identifier not found or not unique.
   --> contracts/TokenFarm.sol:109:28:
    |
109 |     function getTokenValue(_token) public view returns (uint256, uint256) {
    |                            ^^^^^^

La solucion es agregrar address antes de _token

**En este error, cuando declare la funcion no puse "_" en la variable**

 function unstakeTokens(address _token) aca antes de token siempre "_"

DeclarationError: Undeclared identifier. Did you mean "user" or "super"?
  --> contracts/TokenFarm.sol:47:36:
   |
47 |         if (stakingBalance[_token][_user] <= 0) {


**En este error use el indexer en lugar de la lista, por eso el error el indexer no tiene lenght :D, me costo encontrar este/**

TypeError: Member "length" not found or not visible after argument-dependent lookup in uint256.
  --> contracts/TokenFarm.sol:91:34:
   |
91 |             allowedTokensIndex < allowedTokensIndex.length;
   |                                  ^^^^^^^^^^^^^^^^^^^^^^^^^

PS C:\Rust-Crypto\AAT> brownie compile
