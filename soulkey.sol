// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SoulKeyGuardian {
    address public owner;
    address public guardian;
    string public soulMetadataURI;
    bool public active;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event GuardianChanged(address indexed previousGuardian, address indexed newGuardian);
    event SoulMetadataUpdated(string newMetadataURI);
    event SystemDeactivated();

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    modifier onlyGuardian() {
        require(msg.sender == guardian, "Not the guardian");
        _;
    }

    constructor(string memory _soulMetadataURI, address _guardian) {
        owner = msg.sender;
        guardian = _guardian;
        soulMetadataURI = _soulMetadataURI;
        active = true;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Invalid address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    function changeGuardian(address newGuardian) public onlyOwner {
        require(newGuardian != address(0), "Invalid address");
        emit GuardianChanged(guardian, newGuardian);
        guardian = newGuardian;
    }

    function updateSoulMetadata(string memory newMetadataURI) public onlyOwner {
        soulMetadataURI = newMetadataURI;
        emit SoulMetadataUpdated(newMetadataURI);
    }

    function deactivateSystem() public onlyGuardian {
        active = false;
        emit SystemDeactivated();
    }

    function getSoulKeyInfo() public view returns (address, address, string memory, bool) {
        return (owner, guardian, soulMetadataURI, active);
    }
}

