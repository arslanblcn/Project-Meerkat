<template>
    <v-row>
        <v-col cols="12" sm="6">
          <v-card 
        outlined
        width="750"
        height="400"
        class="mt-7">
            <div>
                <apex-chart type="bar" :options="chartOptions" :series="series"></apex-chart>
            </div>
        </v-card>
        </v-col>
        <v-col cols="12" sm="3">
          <v-card 
        outlined
        width="450"
        height="400"
        class="mt-7">
            <div class="mt-6">
                <apex-chart type="pie" :options="plotOptions" :series="anomalies"></apex-chart>
            </div>   
        </v-card>
        </v-col> 
    </v-row>
</template>

<script>
export default {
    data: function() {
      return {
        chartOptions: {
          chart: {
            id: 'vuechart-example'
          },
          xaxis: {
            categories: ['January', 'Fabruary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          },
          title: {
            text: 'Monthly Analysing',
            align: 'center',
            style: {
                fontSize: '13px',
                color: '#4a4c4f' 
            }
          }
        },
        plotOptions: {
            chart: {
                type: "pie",
                },
                title: {
                    text: 'Detected Anomalies',
                    align: 'center',
                    style: {
                        fontSize: '13px',
                        color: '#4a4c4f' 
                    }
                },
                labels: ["Low", "Medium", "High", "Critical"],
                responsive: [
                {
                    options: {
                    legend: {
                        position: "bottom",
                    },
                    },
                },
            ],
        },
        series: [{
          name: 'Number of analysis',
          data: [10,21,6,5,17, 15,64,30, 40, 35, 50, 49]
        }],
        anomalies: [5, 2, 1, 6],
      }
    },
};
</script>