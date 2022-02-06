"use strict";

$(function () {
  chart1();
  chart2();
  smallchart1();
  smallchart2();
  vectormap();

  if ($("#project-team-scroll").length) {
    $("#project-team-scroll")
      .css({
        height: 400,
      })
      .niceScroll();
  }
  if ($("#proTeamScroll").length) {
    $("#proTeamScroll")
      .css({
        height: 400,
      })
      .niceScroll();
  }
  if ($("#top-5-scroll").length) {
    $("#top-5-scroll")
      .css({
        height: 380,
      })
      .niceScroll();
  }
});

function chart1() {
  am4core.ready(function () {
    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    /**
     * Chart design taken from Samsung health app
     */

    var chart = am4core.create("barChart", am4charts.XYChart);
    chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

    chart.data = [
      {
        date: "2000",
        steps: 4561,
      },
      {
        date: "2001",
        steps: 5687,
      },
      {
        date: "2002",
        steps: 6348,
      },
      {
        date: "2003",
        steps: 4878,
      },
      {
        date: "2004",
        steps: 9867,
      },
      {
        date: "2005",
        steps: 7561,
      },
      {
        date: "2006",
        steps: 1287,
      },
      {
        date: "2007",
        steps: 3298,
      },
      {
        date: "2008",
        steps: 5432,
      },
    ];

    chart.dateFormatter.inputDateFormat = "YYYY-MM-dd";
    chart.zoomOutButton.disabled = true;

    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.grid.template.strokeOpacity = 0;
    dateAxis.renderer.minGridDistance = 10;
    dateAxis.dateFormats.setKey("day", "d");
    dateAxis.tooltip.hiddenState.properties.opacity = 1;
    dateAxis.tooltip.hiddenState.properties.visible = true;
    dateAxis.renderer.labels.template.fill = am4core.color("#8e8da4");

    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.renderer.inside = true;
    valueAxis.renderer.grid.template.strokeOpacity = 0;
    valueAxis.min = 0;
    valueAxis.cursorTooltipEnabled = false;
    valueAxis.renderer.labels.template.fill = am4core.color("#8e8da4");

    // goal guides
    var axisRange = valueAxis.axisRanges.create();
    axisRange.value = 6000;
    axisRange.grid.strokeOpacity = 0.1;
    axisRange.label.text = "Goal";
    axisRange.label.align = "right";
    axisRange.label.verticalCenter = "bottom";

    valueAxis.renderer.gridContainer.zIndex = 1;

    var axisRange2 = valueAxis.axisRanges.create();
    axisRange2.value = 12000;
    axisRange2.grid.strokeOpacity = 0.1;
    axisRange2.label.text = "2x goal";
    axisRange2.label.align = "right";
    axisRange2.label.verticalCenter = "bottom";
    axisRange2.label.fillOpacity = 0.8;

    var series = chart.series.push(new am4charts.ColumnSeries());
    series.dataFields.valueY = "steps";
    series.dataFields.dateX = "date";
    series.tooltipText = "{valueY.value}";
    series.tooltip.pointerOrientation = "vertical";
    series.tooltip.hiddenState.properties.opacity = 1;
    series.tooltip.hiddenState.properties.visible = true;

    var columnTemplate = series.columns.template;
    columnTemplate.width = 30;
    columnTemplate.column.cornerRadiusTopLeft = 20;
    columnTemplate.column.cornerRadiusTopRight = 20;
    columnTemplate.strokeOpacity = 0;

    columnTemplate.adapter.add("fill", function (fill, target) {
      var dataItem = target.dataItem;
      if (dataItem.valueY > 6000) {
        return am4core.color("#10CFBD");
      } else {
        return am4core.color("#a8b3b7");
      }
    });

    var cursor = new am4charts.XYCursor();
    cursor.behavior = "panX";
    chart.cursor = cursor;
    cursor.lineX.disabled = true;

    var middleLine = chart.plotContainer.createChild(am4core.Line);
    middleLine.strokeOpacity = 1;
    middleLine.stroke = am4core.color("#000000");
    middleLine.strokeDasharray = "2,2";
    middleLine.align = "center";
    middleLine.zIndex = 1;
    middleLine.adapter.add("y2", function (y2, target) {
      return target.parent.pixelHeight;
    });

    cursor.events.on("cursorpositionchanged", updateTooltip);
    dateAxis.events.on("datarangechanged", updateTooltip);

    function updateTooltip() {
      dateAxis.showTooltipAtPosition(0.5);
      series.showTooltipAtPosition(0.5, 0);
      series.tooltip.validate(); // otherwise will show other columns values for a second
    }
  }); // end am4core.ready()
}

function chart2() {
  am4core.ready(function () {
    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create chart instance
    var chart = am4core.create("lineChart", am4charts.XYChart);

    //

    // Increase contrast by taking evey second color
    chart.colors.step = 2;

    // Add data
    chart.data = generateChartData();

    // Create axes
    var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
    dateAxis.renderer.minGridDistance = 50;
    dateAxis.renderer.labels.template.fill = am4core.color("#8e8da4");

    // Create series
    function createAxisAndSeries(field, name, opposite, bullet) {
      var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      if (chart.yAxes.indexOf(valueAxis) != 0) {
        valueAxis.syncWithAxis = chart.yAxes.getIndex(0);
      }

      var series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.valueY = field;
      series.dataFields.dateX = "date";
      series.strokeWidth = 2;
      series.yAxis = valueAxis;
      series.name = name;
      series.tooltipText = "{name}: [bold]{valueY}[/]";
      series.tensionX = 0.8;
      series.showOnInit = true;

      var interfaceColors = new am4core.InterfaceColorSet();

      switch (bullet) {
        case "rectangle":
          var bullet = series.bullets.push(new am4charts.Bullet());
          bullet.width = 10;
          bullet.height = 10;
          bullet.horizontalCenter = "middle";
          bullet.verticalCenter = "middle";

          var rectangle = bullet.createChild(am4core.Rectangle);
          rectangle.stroke = interfaceColors.getFor("background");
          rectangle.strokeWidth = 2;
          rectangle.width = 10;
          rectangle.height = 10;
          break;
        default:
          var bullet = series.bullets.push(new am4charts.CircleBullet());
          bullet.circle.stroke = interfaceColors.getFor("background");
          bullet.circle.strokeWidth = 2;
          break;
      }

      valueAxis.renderer.line.strokeOpacity = 1;
      valueAxis.renderer.line.strokeWidth = 2;
      valueAxis.renderer.line.stroke = series.stroke;
      valueAxis.renderer.labels.template.fill = series.stroke;
      valueAxis.renderer.opposite = opposite;
    }

    createAxisAndSeries("visits", "Visits", false, "circle");
    createAxisAndSeries("hits", "Hits", true, "rectangle");

    // Add legend
    chart.legend = new am4charts.Legend();

    // Add cursor
    chart.cursor = new am4charts.XYCursor();

    // generate some random data, quite different range
    function generateChartData() {
      var chartData = [];
      var firstDate = new Date();
      firstDate.setDate(firstDate.getDate() - 100);
      firstDate.setHours(0, 0, 0, 0);

      var visits = 1600;
      var hits = 2900;
      var views = 8700;

      for (var i = 0; i < 15; i++) {
        // we create date objects here. In your data, you can have date strings
        // and then set format of your dates using chart.dataDateFormat property,
        // however when possible, use date objects, as this will speed up chart rendering.
        var newDate = new Date(firstDate);
        newDate.setDate(newDate.getDate() + i);

        visits += Math.round(
          (Math.random() < 0.5 ? 1 : -1) * Math.random() * 10
        );
        hits += Math.round((Math.random() < 0.5 ? 1 : -1) * Math.random() * 10);
        views += Math.round(
          (Math.random() < 0.5 ? 1 : -1) * Math.random() * 10
        );

        chartData.push({
          date: newDate,
          visits: visits,
          hits: hits,
          views: views,
        });
      }
      return chartData;
    }
  }); // end am4core.ready()
}

function smallchart1() {
  var options = {
    series: [
      {
        name: "series1",
        data: [81, 90, 78, 101, 92, 109, 100],
      },
      {
        name: "series2",
        data: [70, 82, 95, 82, 84, 102, 91],
      },
    ],
    chart: {
      height: 310,
      type: "area",
      dropShadow: {
        enabled: true,
        opacity: 0.3,
        blur: 5,
        left: -7,
        top: 22,
      },
      toolbar: {
        show: false,
      },
    },
    colors: ["#9D1B69", "#25AF69"],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
    },
    xaxis: {
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      crosshairs: {
        show: true,
      },
      categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
      labels: {
        offsetX: 0,
        offsetY: 5,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-xaxis-title",
        },
      },
    },
    yaxis: {
      labels: {
        offsetX: 0,
        offsetY: 0,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-yaxis-title",
        },
      },
    },
    legend: {
      show: false,
    },
    tooltip: {
      theme: "dark",
      marker: {
        show: true,
      },
      x: {
        show: true,
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#schart1"), options);

  chart.render();
}
function smallchart2() {
  var options = {
    series: [
      {
        name: "series1",
        data: [81, 90, 78, 101, 92, 109, 100],
      },
      {
        name: "series2",
        data: [70, 82, 95, 82, 84, 102, 91],
      },
    ],
    chart: {
      height: 300,
      type: "line",
      dropShadow: {
        enabled: true,
        opacity: 0.3,
        blur: 5,
        left: -7,
        top: 22,
      },
      toolbar: {
        show: false,
      },
    },
    colors: ["#6777EF", "#FEB019"],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: true,
      curve: "smooth",
      width: 3,
      lineCap: "square",
    },
    xaxis: {
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      crosshairs: {
        show: true,
      },
      categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
      labels: {
        offsetX: 0,
        offsetY: 5,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-xaxis-title",
        },
      },
    },
    yaxis: {
      labels: {
        offsetX: 0,
        offsetY: 0,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-yaxis-title",
        },
      },
    },
    legend: {
      show: false,
    },
    tooltip: {
      theme: "dark",
      marker: {
        show: true,
      },
      x: {
        show: true,
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#schart2"), options);
  chart.render();
}

function vectormap() {
  $("#visitorMap").vectorMap({
    map: "world_en",
    zoomButtons: false,
    backgroundColor: "#ffffff",
    borderColor: "#f2f2f2",
    borderOpacity: 0.8,
    borderWidth: 1,
    hoverColor: "#000",
    hoverOpacity: 0.8,
    color: "#ddd",
    normalizeFunction: "linear",
    selectedRegions: false,
    showTooltip: true,
    pins: {
      in: '<div class="jqvmap-circle bg-orange"></div>',
      ca: '<div class="jqvmap-circle bg-green"></div>',
      au: '<div class="jqvmap-circle bg-cyan"></div>',
      ru: '<div class="jqvmap-circle bg-pink"></div>',
      ar: '<div class="jqvmap-circle bg-blue"></div>',
      sy: '<div class="jqvmap-circle bg-teal"></div>',
      ae: '<div class="jqvmap-circle bg-amber"></div>',
      nz: '<div class="jqvmap-circle bg-brown"></div>',
      tl: '<div class="jqvmap-circle bg-indigo"></div>',
      ng: '<div class="jqvmap-circle bg-light-green"></div>',
      si: '<div class="jqvmap-circle bg-grey"></div>',
      pa: '<div class="jqvmap-circle bg-deep-orange"></div>',
    },
  });
}
