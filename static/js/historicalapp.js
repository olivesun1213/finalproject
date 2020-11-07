// from data.js
var tableData = data;

// YOUR CODE HERE!
var filterButton=d3.select("#filter-btn");

filterButton.on("click",function(){
    var hourInput=document.getElementById("hour").value;
    var roadInput=document.getElementById("roadclass").value;
    var trafficInput=document.getElementById("trafficcontrol").value;
    var visibilityInput=document.getElementById("visibility").value;
    var lightInput=document.getElementById("light").value;
    var conditionInput=document.getElementById("condition").value;
    console.log(hourInput);
    console.log(roadInput);
    console.log(trafficInput);
    console.log(visibilityInput);
    console.log(lightInput);
    console.log(conditionInput);
    
    var dataFiltered=tableData.filter(record => (record.VISIBILITY == visibilityInput || visibilityInput == "") && (record.LIGHT == lightInput || lightInput == "")
    && (record.RDSFCOND == conditionInput || conditionInput == "") && (record.HOUR == hourInput || hourInput == "") && (record.ROAD_CLASS == roadInput || roadInput=="") 
    && (record.TRAFFCTL == trafficInput || trafficInput == ""));
    console.log(dataFiltered);

    var tbody=d3.select("tbody");
    tbody.html("");       
    dataFiltered.forEach(element => {
        var row=tbody.append("tr");
        row.append("td").text(element.DATE.split(" ",1));
        row.append("td").text(element.HOUR);
        row.append("td").text(element.STREET1);        
        row.append("td").text(element.LATITUDE);
        row.append("td").text(element.LONGITUDE);
        row.append("td").text(element.Neighbourhood);
        row.append("td").text(element.ACCLASS);
    })
})
