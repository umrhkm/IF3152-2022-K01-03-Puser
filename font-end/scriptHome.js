const tombolDineIn = document.getElementsByClassName("toggle dine-in")[0]
const tombolTakeAway = document.getElementsByClassName("toggle take-away")[0]
const tombolHomeContainer = document.querySelector(".home-tombol-DiTa-container")
const inputNomorMeja = document.getElementById("input-nomor-meja")

const listButton = [tombolDineIn,tombolTakeAway]


listButton.forEach(toggle => {

    toggle.addEventListener("click", () => {
        console.log(inputNomorMeja.value)
        if (toggle.className.includes("active")){
            
        }else{
            if (toggle.className.includes("dine-in")){
                tombolTakeAway.classList.toggle('active')
                inputNomorMeja.style.transform = "translate(0, -90px)"
                setTimeout(()=>{inputNomorMeja.style.display = "flex"}, 100)
                setTimeout(()=>{inputNomorMeja.style.transform = "translate(0, 0)"}, 300)
                

            } else if (toggle.className.includes("take-away")){
                tombolDineIn.classList.toggle('active')
                inputNomorMeja.style.transform = "translate(0, -90px)"
                setTimeout(()=>{inputNomorMeja.style.display = "none"}, 300)
            }
            toggle.classList.toggle('active')
        }

        

    })
})