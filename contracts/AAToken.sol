pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract AAToken is ERC20 {
    constructor() public ERC20("Argentinian Art Token", "AAT"){
        _mint(msg.sender,2780400000000000000000000000);
    }
}