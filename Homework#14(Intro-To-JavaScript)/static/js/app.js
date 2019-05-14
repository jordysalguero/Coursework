// from data.js
var tableData = data;

// table reference
var table = d3.select("#ufo-table")
// tbody reference
var tbody = table.select("tbody")

// Add Data to HTML Page
// Loop through each data entry
function tableCreation(data) {

    data.forEach(entry => {
        var row = tbody.append("tr")
        // Use 'Object.entries' to add the values to each row
        Object.entries(entry).forEach(function([key, value]) {
        // Append a cell to the row for each value
        var cell = row.append("td")
        // Add the values to each cell
            cell.text(value)
        })
    })
}

tableCreation(tableData)

// Select the submit button
var submit = d3.select("#filter-btn")

// Select the input element and get the raw HTML node
var inputElement = d3.select("#datetime")

// Create submit function event handler
submit.on("click", function(){
    
    // Clear out previous table
    tbody.text("")

    //Prevent page from refreshing
    d3.event.preventDefault()

    // Get the property of the input element
    var inputValue = inputElement.property("value")

    // Filter the data to match the inputValue
    var filteredData = data.filter(entry => entry.datetime === inputValue)

    // Create table
    tableCreation(filteredData)
})


