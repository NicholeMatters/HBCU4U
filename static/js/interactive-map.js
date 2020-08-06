$(document).ready(function() {
  let city, map;
  map = $('.ct-map');
  city = map.find('.ct-city');
  city.each(function() {
    let button, that;
    that = $(this);
    button = that.find('.ct-city__button');
    return button.on('click', function() {
      city.not(that).removeClass('active');
      if (that.hasClass('active')) {
        that.removeClass('active');
        return map.removeClass('popup-open');
      } else {
        that.addClass('active');
        return map.addClass('popup-open');
      }
    });
  });
});

// / JS 
// let chartConfig = { 
//   debug: true, 
//   title_label_text: 
//     '2012 Presidential Election Results', 
//   type: 'map', 
//   axisToZoom: '', 
//   toolbar_visible: false, 
//   legend: { 
//     position: 'inside top right', 
//     margin: { top: -10, right: 100 }, 
//     layout: 'horizontal', 
//     defaultEntry_style_fontSize: '14px'
//   }, 
//   defaultPoint: { 
//     outline_color: 'white', 
//     label: { 
//       text: '%stateCode', 
//       style_color: '#3a3a3a'
//     }, 
//     tooltip: 
//       '%name<br/><b>Obama:</b> %obama%<br/><b>Romney:</b> %romney%<br/><b>Winner:</b> %seriesName'
//   }, 
//   series: [ 
//     { 
//       name: 'Romney', 
//       color: '#bb4e55', 
//       points: [] 
//     }, 
//     { 
//       name: 'Obama', 
//       color: '#40698b', 
//       points: [] 
//     } 
//   ] 
// }; 
// //State, Obama, Romney % 
// let results = [ 
//   ['Alabama', 38.36, 60.55], 
//   ['Alaska', 40.81, 54.8], 
//   ['Arizona', 44.45, 53.48], 
//   ['Arkansas', 36.88, 60.57], 
//   ['California', 60.16, 37.07], 
//   ['Colorado', 51.45, 46.09], 
//   ['Connecticut', 58.06, 40.72], 
//   ['Delaware', 58.61, 39.98], 
//   ['D. C.', 90.91, 7.28], 
//   ['Florida', 49.9, 49.03], 
//   ['Georgia', 45.39, 53.19], 
//   ['Hawaii', 70.55, 27.84], 
//   ['Idaho', 32.4, 64.09], 
//   ['Illinois', 57.5, 40.66], 
//   ['Indiana', 43.84, 54.04], 
//   ['Iowa', 51.99, 46.18], 
//   ['Kansas', 38.0, 59.59], 
//   ['Kentucky', 37.78, 60.47], 
//   ['Louisiana', 40.58, 57.78], 
//   ['Maine', 56.27, 40.98], 
//   ['Maryland', 61.97, 35.9], 
//   ['Massachusetts', 60.67, 37.52], 
//   ['Michigan', 54.04, 44.58], 
//   ['Minnesota', 52.65, 44.96], 
//   ['Mississippi', 43.79, 55.29], 
//   ['Missouri', 44.28, 53.64], 
//   ['Montana', 41.66, 55.3], 
//   ['Nebraska', 38.03, 59.8], 
//   ['Nevada', 52.36, 45.68], 
//   ['New Hampshire', 51.98, 46.4], 
//   ['New Jersey', 58.25, 40.5], 
//   ['New Mexico', 52.99, 42.84], 
//   ['New York', 63.35, 35.17], 
//   ['North Carolina', 48.35, 50.39], 
//   ['North Dakota', 38.69, 58.32], 
//   ['Ohio', 50.58, 47.6], 
//   ['Oklahoma', 33.23, 66.77], 
//   ['Oregon', 54.24, 42.15], 
//   ['Pennsylvania', 51.95, 46.57], 
//   ['Rhode Island', 62.7, 35.24], 
//   ['South Carolina', 44.09, 54.56], 
//   ['South Dakota', 39.87, 57.89], 
//   ['Tennessee', 39.04, 59.42], 
//   ['Texas', 41.35, 57.13], 
//   ['Utah', 24.67, 72.55], 
//   ['Vermont', 66.57, 30.97], 
//   ['Virginia', 51.16, 47.28], 
//   ['Washington', 55.8, 41.03], 
//   ['West Virginia', 35.45, 62.14], 
//   ['Wisconsin', 52.83, 45.89], 
//   ['Wyoming', 27.82, 68.64] 
// ]; 
// let romneySeries = chartConfig.series[0]; 
// let obamaSeries = chartConfig.series[1]; 
  
// for ( 
//   let i = 0, iLen = results.length; 
//   i < iLen; 
//   i++ 
// ) { 
//   let stateRes = results[i]; 
//   if (stateRes[2] > stateRes[1]) { 
//     romneySeries.points.push({ 
//       map: 'US.name:' + stateRes[0], 
//       attributes: { 
//         obama: stateRes[1], 
//         romney: stateRes[2] 
//       } 
//     }); 
//   } else { 
//     obamaSeries.points.push({ 
//       map: 'US.name:' + stateRes[0], 
//       attributes: { 
//         obama: stateRes[1], 
//         romney: stateRes[2] 
//       } 
//     }); 
//   } 
// } 
  
// let chart = JSC.chart('chartDiv', chartConfig); 