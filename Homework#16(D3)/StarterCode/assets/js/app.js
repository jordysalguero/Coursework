// Create SVG box
var svgWidth = 960;
var svgHeight = 500;

var margin = { 
  top: 20, 
  right: 40, 
  bottom: 80, 
  left: 100 
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)
  .append("g")

// Append an SVG Group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Define the div for the tooltip
var toolTip = d3.select("body")
    .append("div")	
    .classed("tooltip", true)
    .attr("fill", "blue")


d3.csv("./assets/data/data.csv").then(function(Data) {

  Data.forEach(function(data) {
    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare;
  });

  // Create scale functions
  var yLinearScale = d3.scaleLinear()
    .range([height, 0]);

  var xLinearScale = d3.scaleLinear()
    .range([0, width]);

  // Create axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Scale the domain
  xLinearScale.domain([8, d3.max(Data, function(data) {
    return +data.poverty;
  })]);
  yLinearScale.domain([0, d3.max(Data, function(data) {
    return +data.healthcare * 1.2;
  })]);
  
  // Add the scatterplot
  var dots = chartGroup.selectAll("circle")
    .data(Data)
    .enter()
    .append("circle")
    .attr("cx", function(d) { return xLinearScale(d.poverty)})
    .attr("cy", function(d) { return yLinearScale(d.healthcare)})
    .attr("r", 15)
    .attr("fill", "SkyBlue")

    dots.on("mouseover", function(d) {		
    toolTip.transition()
      .duration(100)
      .style("opacity", 100)
    toolTip.html(`${d.abbr}<br>Poverty:${d.poverty}<br>Healthcare:${d.healthcare}`)
      .style("left", (d3.event.pageX) + "px")
      .style("top", (d3.event.pageY) + "px")
        })
      .on("mouseout", function(d) {		
    toolTip.transition()
      .duration(500)
      .style("opacity", 0);	
      });
    
    // dots.append("text")
    // .attr("font-size", 500)
    // .attr("class", "stateText")
    // .attr("dx", function(d) {
    //    return xLinearScale(d.poverty);
    // })
    // .attr("dy", function(d) {
    //   // Push text to center by a 1/3
    //   return yLinearScale (d.healthcare)/3;
    // })
    // .text(function(d) {
    //     return d.abbr;
    //   })

  // Add the X-axis
  var xAxis = chartGroup.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(bottomAxis)
  
  // Add the Y-axis
  var yAxis = chartGroup.append("g")
    .attr("class", "y axis")
    .call(leftAxis)

// Append y-axis labels
  chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2)- 60)
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)")
      .attr("font-weight", "bold");

// Append x-axis labels
  chartGroup.append("text")
    .attr("transform", "translate(" + (width / 2 - 25) + " ," + (height + margin.top + 30) + ")")
    .attr("class", "axisText")
    .text("In Poverty (%)")
    .attr("font-weight", "bold")
});
