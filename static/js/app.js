
// function init() {
    
//     d3.json("/ocr").then(dataInit => {
//       data = dataInit;
        
//       // look at keys to grab correct parameter
//       var selection = dataInit.names;
//       var selector = d3.select("#selDataset");
        
//       selection.forEach(value => {
//         selector
//           .append("option")
//           .text(value)
//           .attr("value", function() {
//             return value;
//           });
//       });
//     });
//   }

// init();