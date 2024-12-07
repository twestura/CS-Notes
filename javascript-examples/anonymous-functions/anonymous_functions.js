function compare(x, y) {
  return x - y;
}
console.log([5, 7, 3, 2, 9].sort(compare));

// Using an anonymous function.
console.log([5, 7, 3, 2, 9].sort((x, y) => x - y));
