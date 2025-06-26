// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MedOracle {
    struct Report {
        string risk;
        string ipfsHash;
        uint timestamp;
    }

    mapping(address => Report[]) public reports;

    function addReport(string memory _risk, string memory _ipfsHash) public {
        reports[msg.sender].push(Report(_risk, _ipfsHash, block.timestamp));
    }

    function getReports(address _user) public view returns (Report[] memory) {
        return reports[_user];
    }
}
