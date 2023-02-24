function decimalToGray(decimal) {
    return decimal ^ (decimal >> 1);
  }
  
  // Example usage
  console.log(decimalToGray(10)); // Outputs 15
  