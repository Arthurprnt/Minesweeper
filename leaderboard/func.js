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

data = [
]

data.sort()

for (let i = 0; i < data.length; i++) {

  const card = userCardTemplate.content.cloneNode(true).children[0]
  const header = card.querySelector("[data-header]")
  header.textContent = `${data[i][2]} - ${data[i][0]} - ${data[i][1]}`
  userCardContainer.append(card)
  users.push({name: `${data[i][2]} - ${data[i][1]}`, element: card})

}