const userCardTemplate = document.querySelector("[data-user-template]")
const userCardContainer = document.querySelector("[data-user-cards-container]")
const searchInput = document.querySelector("[data-search]")

let users = []

searchInput.addEventListener("input", (e) => {
    const value = e.target.value.toLowerCase()
    users.forEach(user => {
        const isVisible = user.name.toLowerCase().includes(value)
        user.element.classList.toggle("hide", !isVisible)
    })
})

var currentDirectory = window.location.pathname.split('/').slice(0, -1).join('/');
console.log(`${currentDirectory}/assets/stats.csv`)

onload = fetch(`file:/${currentDirectory}/assets/stats.csv`)

    .then(res => {return res.text()})
    .then(data => {

        console.log(data)

})