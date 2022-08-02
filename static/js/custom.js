var isMoving = false;
function autoModeClick() {
    var measurementControlSection = document.getElementById("measurementControlSection");
    measurementControlSection.innerHTML = `
        <label for="measurements1" class="form-label">Liczba pomiarów</label>
        <input type="number" class="form-control" id="measurements1" aria-describedby="measurements1Help" min="2" max="100">
        <div id="measurements1Help" class="form-text">Pomiary będą rozmieszczone równomiernie na okręgu.
        Przedział 2-100</div>
        <button type="button" class="btn btn-primary" id="measurmentGoButton" onclick="measurementStartClick()">Go</button>
        <button type="button" class="btn btn-success" id="measurmentNextButton" onclick="measurementNextClick() disabled">Następny punkt</button>`;
}

function auto3DModeClick() {
    var measurementControlSection = document.getElementById("measurementControlSection");
    measurementControlSection.innerHTML = `
        <label for="measurements1" class="form-label">Liczba pomiarów na okręgu</label>
        <input type="number" class="form-control" id="measurements1" aria-describedby="measurements1Help" min="2" max="100">
        <div id="measurements1Help" class="form-text pb-3">Pomiary będą rozmieszczone równomiernie na okręgu. Przedział 2-100</div>
        <label for="measurements2" class="form-label pt-3">Liczba pomiarów pionowych</label>
        <input type="number" class="form-control" id="measurements2" aria-describedby="measurements2Help" min="2" max="100">
        <div id="measurements2Help" class="form-text">Pomiary rozmieszczone równo na przedziale (x, Y). Przedział 2-100 punktów</div>
        <button type="button" class="btn btn-primary" id="measurmentGoButton" onclick="measurementStartClick()">Go</button>`;
}

function manualModeClick() {
    var measurementControlSection = document.getElementById("measurementControlSection");
    measurementControlSection.innerHTML = `
        <label for="measurements1" class="form-label">Podaj kąt o który chcesz przesunąć ramię:</label>
        <input type="number" class="form-control" id="measurements1" aria-describedby="measurements1Help" min="1" max="360">
        <div id="measurements1Help" class="form-text pb-3">ruch zgodnie ze wskazówkami zegara</div>
        <button type="button" class="btn btn-primary" id="measurmentGoButton" onclick="measurementStartClick()">Go</button>`;
}

function measurementStartClick(){
    if(isMoving == false){
        isMoving = true
        checkState()
        document.querySelector('#measurmentGoButton').disabled = true
        $.get('_moveSteppers', {angle: document.getElementById('measurements1').value })
    }
}

//this function should check the state of the device
function checkState(){
    var stateField = document.getElementById("stateField");
    var interval = setInterval(function(){
        $.ajax({
          url: "/_checkState",
          type: "get",
          success: function(response) {
            if(response == "0"){
                stateField.innerHTML = `<button type="button" class="btn btn-danger" style="pointer-events: none;" id="stateDanger">Błąd</button>`;
            }else if(response == "1"){
                stateField.innerHTML = `<button type="button" class="btn btn-success" style="pointer-events: none;" id="stateReady">Gotowy</button>`;
                isMoving = false; 
                document.querySelector('#measurmentGoButton').disabled = false
                clearInterval(interval)
            }else if(response == "2"){
                stateField.innerHTML = `
                <button class="btn btn-primary" type="button" style="pointer-events: none;" id="stateMoving">
                <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                Obracanie
                </button>`;
                isMoving = true;  
            }
           },
          error: function(xhr) {
              //Handel error
          }
        }); 
    }, 1000);
}

