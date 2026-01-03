const $ = s => document.querySelector(s)

let students = []
let edit = null

$("#studentForm").addEventListener("submit", e => {
    e.preventDefault()
    const data = Object.fromEntries(new FormData(e.target))
    edit !== null ? students[edit] = data : students.push(data)
    edit = null
    e.target.reset()
    render()
})

$("#sort").onclick = () => {
    students.sort((a,b) => a.grade - b.grade)
    render()
}

$("#filter").onchange = e => {
    render(e.target.value)
}

$("#list").onclick = e => {
    if (e.target.dataset.edit) {
        edit = e.target.dataset.edit
        Object.entries(students[edit])
            .forEach(([k,v]) => studentForm[k].value = v)
    }

    if (e.target.dataset.del) {
        students.splice(e.target.dataset.del, 1)
        render()
    }
}

function render(subject = "") {
    $("#list").innerHTML = ""
    $("#filter").innerHTML = `<option value="">All</option>`

    students
        .filter(s => !subject || s.subject === subject)
        .forEach((s,i) => {
            $("#filter").innerHTML += `<option>${s.subject}</option>`
            $("#list").innerHTML += `
                <tr>
                    <td>${s.firstName}</td>
                    <td>${s.grade}</td>
                    <td>${s.subject}</td>
                    <td>
                        <button data-edit="${i}">Edit</button>
                        <button data-del="${i}">Delete</button>
                    </td>
                </tr>
            `
        })
}