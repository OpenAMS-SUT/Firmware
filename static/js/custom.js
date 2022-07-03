var isMoving = false;
function autoModeClick() {
    var measurementControlSection = document.getElementById("measurementControlSection");
    measurementControlSection.innerHTML = `
        <label for="measurements1" class="form-label">Liczba pomiarów</label>
        <input type="number" class="form-control" id="measurements1" aria-describedby="measurements1Help" min="2" max="100">
        <div id="measurements1Help" class="form-text">Pomiary będą rozmieszczone równomiernie na okręgu.
        Przedział 2-100</div>`;
}

function auto3DModeClick() {
    var measurementControlSection = document.getElementById("measurementControlSection");
    measurementControlSection.innerHTML = `
        <label for="measurements1" class="form-label">Liczba pomiarów na okręgu</label>
        <input type="number" class="form-control" id="measurements1" aria-describedby="measurements1Help" min="2" max="100">
        <div id="measurements1Help" class="form-text pb-3">Pomiary będą rozmieszczone równomiernie na okręgu. Przedział 2-100</div>
        <label for="measurements2" class="form-label pt-3">Liczba pomiarów pionowych</label>
        <input type="number" class="form-control" id="measurements2" aria-describedby="measurements2Help" min="2" max="100">
        <div id="measurements2Help" class="form-text">Pomiary rozmieszczone równo na przedziale (x, Y). Przedział 2-100 punktów</div>`;
}

function manualModeClick() {
    var measurementControlSection = document.getElementById("measurementControlSection");
    measurementControlSection.innerHTML = "To be implemented or not to be implemented";
}

function measurementStartClick(){
    var stateField = document.getElementById("stateField");
if(isMoving){
    stateField.innerHTML = `
        <button class="btn btn-primary" type="button" style="pointer-events: none;" id="stateMoving">
        <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
        Obracanie
        </button>`;
    isMoving = false;
}else{
    stateField.innerHTML = `<button type="button" class="btn btn-success" style="pointer-events: none;" id="stateReady">Gotowy</button>`;
    isMoving = true;
}

//this function should check the state of the device
function checkState(){

}
}