// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MedOracle {
    struct Report {
        string risk;         // "RISK_HIGH" or "RISK_LOW"
        string ipfsHash;     // IPFS CID of the report
        uint256 timestamp;   // When the record was stored
    }

    mapping(address => Report[]) public reports;

    event ReportStored(address indexed user, string risk, string ipfsHash, uint256 timestamp);

    function storeReport(string memory risk, string memory ipfsHash) public {
        reports[msg.sender].push(Report(risk, ipfsHash, block.timestamp));
        emit ReportStored(msg.sender, risk, ipfsHash, block.timestamp);
    }

    function getReports(address user) public view returns (Report[] memory) {
        return reports[user];
    }
}
