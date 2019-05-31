// @TODO: YOUR CODE HERE!
d3.csv("../data/data.csv", function(data) {
  //if (error) return console.warn(error);

  console.log(data);
}).catch(error => {
  console.log(error)
})
