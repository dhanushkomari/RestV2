"use strict";

$(function () {
  smallchart1();
  smallchart2();
  smallchart3();
  smallchart4();
  chart1();
  chart2();
});

function smallchart1() {
  var balance_chart = document.getElementById("smallChart1").getContext("2d");

  var balance_chart_bg_color = balance_chart.createLinearGradient(0, 0, 0, 70);
  balance_chart_bg_color.addColorStop(0, "rgba(156,39,176,.2)");
  balance_chart_bg_color.addColorStop(1, "rgba(156,39,176,0)");

  var myChart = new Chart(balance_chart, {
    type: "line",
    data: {
      labels: [
        "16-07-2018",
        "17-07-2018",
        "18-07-2018",
        "19-07-2018",
        "20-07-2018",
        "21-07-2018",
        "22-07-2018",
        "23-07-2018",
        "24-07-2018",
        "25-07-2018",
        "26-07-2018",
        "27-07-2018",
        "28-07-2018",
        "29-07-2018",
        "30-07-2018",
        "31-07-2018",
      ],
      datasets: [
        {
          label: "Balance",
          data: [
            50,
            61,
            80,
            50,
            72,
            52,
            60,
            41,
            30,
            45,
            70,
            40,
            93,
            63,
            50,
            62,
          ],
          backgroundColor: balance_chart_bg_color,
          borderWidth: 3,
          borderColor: "#9c27b0 ",
          pointBorderWidth: 0,
          pointBorderColor: "transparent",
          pointRadius: 3,
          pointBackgroundColor: "transparent",
          pointHoverBackgroundColor: "rgba(63,82,227,1)",
        },
      ],
    },
    options: {
      layout: {
        padding: {
          bottom: -1,
          left: -1,
        },
      },
      legend: {
        display: false,
      },
      scales: {
        yAxes: [
          {
            gridLines: {
              display: false,
              drawBorder: false,
            },
            ticks: {
              beginAtZero: true,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
            ticks: {
              display: false,
            },
          },
        ],
      },
    },
  });
}

function smallchart2() {
  var balance_chart = document.getElementById("smallChart2").getContext("2d");

  var balance_chart_bg_color = balance_chart.createLinearGradient(0, 0, 0, 70);
  balance_chart_bg_color.addColorStop(0, "rgba(255,87,34,.2)");
  balance_chart_bg_color.addColorStop(1, "rgba(255,87,34,0)");

  var myChart = new Chart(balance_chart, {
    type: "line",
    data: {
      labels: [
        "16-07-2018",
        "17-07-2018",
        "18-07-2018",
        "19-07-2018",
        "20-07-2018",
        "21-07-2018",
        "22-07-2018",
        "23-07-2018",
        "24-07-2018",
        "25-07-2018",
        "26-07-2018",
        "27-07-2018",
        "28-07-2018",
        "29-07-2018",
        "30-07-2018",
        "31-07-2018",
      ],
      datasets: [
        {
          label: "Balance",
          data: [
            50,
            61,
            80,
            50,
            72,
            52,
            60,
            41,
            30,
            45,
            70,
            40,
            93,
            63,
            50,
            62,
          ],
          backgroundColor: balance_chart_bg_color,
          borderWidth: 3,
          borderColor: "#ff9800",
          pointBorderWidth: 0,
          pointBorderColor: "transparent",
          pointRadius: 3,
          pointBackgroundColor: "transparent",
          pointHoverBackgroundColor: "rgba(63,82,227,1)",
        },
      ],
    },
    options: {
      layout: {
        padding: {
          bottom: -1,
          left: -1,
        },
      },
      legend: {
        display: false,
      },
      scales: {
        yAxes: [
          {
            gridLines: {
              display: false,
              drawBorder: false,
            },
            ticks: {
              beginAtZero: true,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
            ticks: {
              display: false,
            },
          },
        ],
      },
    },
  });
}
function smallchart3() {
  var balance_chart = document.getElementById("smallChart3").getContext("2d");

  var balance_chart_bg_color = balance_chart.createLinearGradient(0, 0, 0, 70);
  balance_chart_bg_color.addColorStop(0, "rgba(76,175,80,.2)");
  balance_chart_bg_color.addColorStop(1, "rgba(76,175,80,0)");

  var myChart = new Chart(balance_chart, {
    type: "line",
    data: {
      labels: [
        "16-07-2018",
        "17-07-2018",
        "18-07-2018",
        "19-07-2018",
        "20-07-2018",
        "21-07-2018",
        "22-07-2018",
        "23-07-2018",
        "24-07-2018",
        "25-07-2018",
        "26-07-2018",
        "27-07-2018",
        "28-07-2018",
        "29-07-2018",
        "30-07-2018",
        "31-07-2018",
      ],
      datasets: [
        {
          label: "Balance",
          data: [
            50,
            61,
            80,
            50,
            72,
            52,
            60,
            41,
            30,
            45,
            70,
            40,
            93,
            63,
            50,
            62,
          ],
          backgroundColor: balance_chart_bg_color,
          borderWidth: 3,
          borderColor: "#4caf50",
          pointBorderWidth: 0,
          pointBorderColor: "transparent",
          pointRadius: 3,
          pointBackgroundColor: "transparent",
          pointHoverBackgroundColor: "rgba(63,82,227,1)",
        },
      ],
    },
    options: {
      layout: {
        padding: {
          bottom: -1,
          left: -1,
        },
      },
      legend: {
        display: false,
      },
      scales: {
        yAxes: [
          {
            gridLines: {
              display: false,
              drawBorder: false,
            },
            ticks: {
              beginAtZero: true,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
            ticks: {
              display: false,
            },
          },
        ],
      },
    },
  });
}
function smallchart4() {
  var balance_chart = document.getElementById("smallChart4").getContext("2d");

  var balance_chart_bg_color = balance_chart.createLinearGradient(0, 0, 0, 70);
  balance_chart_bg_color.addColorStop(0, "rgba(63,82,227,.2)");
  balance_chart_bg_color.addColorStop(1, "rgba(63,82,227,0)");

  var myChart = new Chart(balance_chart, {
    type: "line",
    data: {
      labels: [
        "16-07-2018",
        "17-07-2018",
        "18-07-2018",
        "19-07-2018",
        "20-07-2018",
        "21-07-2018",
        "22-07-2018",
        "23-07-2018",
        "24-07-2018",
        "25-07-2018",
        "26-07-2018",
        "27-07-2018",
        "28-07-2018",
        "29-07-2018",
        "30-07-2018",
        "31-07-2018",
      ],
      datasets: [
        {
          label: "Balance",
          data: [
            50,
            61,
            80,
            50,
            72,
            52,
            60,
            41,
            30,
            45,
            70,
            40,
            93,
            63,
            50,
            62,
          ],
          backgroundColor: balance_chart_bg_color,
          borderWidth: 3,
          borderColor: "rgba(63,82,227,1)",
          pointBorderWidth: 0,
          pointBorderColor: "transparent",
          pointRadius: 3,
          pointBackgroundColor: "transparent",
          pointHoverBackgroundColor: "rgba(63,82,227,1)",
        },
      ],
    },
    options: {
      layout: {
        padding: {
          bottom: -1,
          left: -1,
        },
      },
      legend: {
        display: false,
      },
      scales: {
        yAxes: [
          {
            gridLines: {
              display: false,
              drawBorder: false,
            },
            ticks: {
              beginAtZero: true,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
            ticks: {
              display: false,
            },
          },
        ],
      },
    },
  });
}

function chart1() {
  var options = {
    series: [
      {
        name: "Net Profit",
        data: [36, 65, 45, 36, 61, 58, 45, 60, 52],
      },
    ],
    chart: {
      type: "bar",
      height: 350,
      dropShadow: {
        enabled: true,
        opacity: 0.3,
        blur: 2,
        left: -10,
        top: 22,
      },
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "30%",
        endingShape: "rounded",
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ["transparent"],
    },
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "july",
        "aug",
        "sep",
      ],
      labels: {
        offsetX: 0,
        offsetY: 0,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-xaxis-title",
        },
      },
    },
    yaxis: {
      title: {
        text: "$ (thousands)",
      },
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
    fill: {
      type: "gradient",
      gradient: {
        shade: "light",
        type: "verticle",
        shadeIntensity: 0.25,
        gradientToColors: undefined,
        inverseColors: false,
        opacityFrom: 0.85,
        opacityTo: 0.85,
        stops: [0, 90, 100],
      },
      colors: ["#6777EF"],
    },
    tooltip: {
      theme: "dark",
      marker: {
        show: true,
      },
      x: {
        show: true,
      },
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands";
        },
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#chart1"), options);
  chart.render();
}
function chart2() {
  var options = {
    series: [
      {
        name: "Income",
        type: "line",
        data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
      },
      {
        name: "Expense",
        type: "area",
        data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
      },
    ],
    chart: {
      height: 350,
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
      stacked: false,
    },
    colors: ["#6777EF", "#FEB019"],
    stroke: {
      width: [5, 5],
      curve: "smooth",
    },
    plotOptions: {
      bar: {
        columnWidth: "50%",
      },
    },

    fill: {
      opacity: [0.85, 0.25, 1],
      gradient: {
        inverseColors: false,
        shade: "light",
        type: "vertical",
        opacityFrom: 0.85,
        opacityTo: 0.55,
        stops: [0, 100, 100, 100],
      },
    },
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "sep",
      "oct",
      "nov",
    ],
    markers: {
      size: 0,
    },
    xaxis: {
      labels: {
        offsetX: 0,
        offsetY: 0,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-xaxis-title",
        },
      },
    },
    yaxis: {
      title: {
        text: "Dollers",
      },
      labels: {
        offsetX: 0,
        offsetY: 0,
        style: {
          fontSize: "12px",
          fontFamily: "Segoe UI",
          cssClass: "apexcharts-yaxis-title",
        },
      },
      min: 0,
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

  var chart = new ApexCharts(document.querySelector("#chart2"), options);
  chart.render();
}
