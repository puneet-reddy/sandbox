/*
    Simple test to see if we can load individual sheets from tableau.
*/

const tableau_url = "https://aidashboard.arubanetworks.com/views/ArubaStrategicDashboards/ArubaSummary";

function init_viz() {
    var tab_viz = $('#tabview');
    let options = {
        width: "100%",
        height: "100%",
        hideTabs: true,
        hideToolbar: true,
        onFirstInteractive: () => {
            workbook = viz.getWorkbook();
            activeSheet = workbook.getActiveSheet();
        }
    };
    viz = new tableau.Viz(tab_viz, tableau_url, options);
}

$(window).on('load', () => {
    init_viz();
});