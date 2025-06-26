async function main() {
  const MedOracle = await ethers.getContractFactory("MedOracle");
  const contract = await MedOracle.deploy();
  await contract.deployed();
  console.log("✅ MedOracle deployed to:", contract.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
