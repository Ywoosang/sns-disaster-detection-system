export default {
    isViewModal: false,
    isSendMail: false,
    // data from crawling
    crawlingData: [],
    // line chart data
    lineData: {
        labels: [],
        datasets: [
          {
            label: "폭설",
            backgroundColor: "rgba(209, 216, 224, 0.2)",
            borderColor: "rgba(209, 216, 224,0.7)", // 흰
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "코로나",
            backgroundColor: "rgba(252, 92, 101, 0.2)",
            borderColor: "rgba(252, 92, 101,0.7)", // 빨
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "교통사고",
            backgroundColor: "rgba(69, 170, 242, 0.2)",
            borderColor: "rgba(69, 170, 242,0.7)", // 파
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "산불",
            backgroundColor: "rgba(253, 150, 68, 0.2)",
            borderColor: "rgba(253, 150, 68,0.7)", // 주
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "붕괴",
            backgroundColor: "rgba(254, 211, 48,0.2)",
            borderColor: "rgba(254, 211, 48,0.7)", //노
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "폭발",
            backgroundColor: "rgba(38, 222, 129, 0.2)",
            borderColor: "rgba(38, 222, 129,0.7)", //초
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "화재",
            backgroundColor: "rgba(165, 94, 234, 0.2)",
            borderColor: "rgba(165, 94, 234,0.7)", //보
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "태풍",
            backgroundColor: "rgba(119, 140, 163, 0.2)",
            borderColor: "rgba(119, 140, 163,0.7)", //회
            borderwidth: 1,
            fill: false,
            data: [],
          },
          {
            label: "홍수",
            backgroundColor: "rgba(75, 123, 236, 0.2)",
            borderColor: "rgba(75, 123, 236, 0.7)", //남
            borderwidth: 1,
            fill: false,
            data: [],
          },
        ],
    },
    lineOptions: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
            display: false
        },
        tooltips: {
            backgroundColor: "rgb(23,30,39)",
            bodyFontColor: "rgba(255, 255, 255, 0.68)",
            titleFontColor: "rgba(255, 255, 255, 0.88)",
        },
    },
    // bar chart data
    barData: {
        labels: [
          "폭설",
          "코로나",
          "교통사고",
          "산불",
          "붕괴",
          "폭발",
          "화재",
          "태풍",
          "홍수",
        ],
        datasets: [
            {
                label: "언급량",
                data: [],
                backgroundColor: [
                "rgba(209, 216, 224,0.2)", // 흰
                "rgba(252, 92, 101,0.2)", // 빨
                "rgba(69, 170, 242,0.2)", // 파
                "rgba(253, 150, 68,0.2)", // 주
                "rgba(254, 211, 48,0.2)", //노
                "rgba(38, 222, 129,0.2)", //초
                "rgba(165, 94, 234,0.2)", //보
                "rgba(119, 140, 163,0.2)", //회
                "rgba(75, 123, 236,0.2)", //남
                ],
                borderColor: [
                "rgba(209, 216, 224,1)", // 흰
                "rgba(252, 92, 101,1)", // 빨
                "rgba(69, 170, 242,1)", // 파
                "rgba(253, 150, 68,1)", // 주
                "rgba(254, 211, 48,1)", //노
                "rgba(38, 222, 129,1)", //초
                "rgba(165, 94, 234,1)", //보
                "rgba(119, 140, 163,1)", //회
                "rgba(75, 123, 236,1)", //남
                ],
                borderWidth: 1,
            },
        ],
    },
    // ranking data
    rankData: [
        "코로나",
        "붕괴",
        "폭설",
        "교통사고",
        "산불",
        "화재",
        "폭발",
        "홍수",
        "태풍"
    ],
    // keywords
    keywords: [
        "폭설",
        "코로나",
        "교통사고",
        "산불",
        "붕괴",
        "폭발",
        "화재",
        "태풍",
        "홍수"
    ],
    // data from model
    modelData: [],
    snsData: [],
    snsInstagram: [],
    snsTwitter: [],
    snsNaver: []
}