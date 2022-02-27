//This will mock FAU Token
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol"; //withou I

contract MockWETH is ERC20 {
    constructor() public ERC20("Mock Weth", "WETH") {}
}
