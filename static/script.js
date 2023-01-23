function myfunction() {
    year = document.querySelector('input[name="year"]:checked').value
    

    var checkboxes = document.getElementsByName('check')
    var courses_string = ''
    for (var checkbox of checkboxes) {
        if (checkbox.checked == true) {
            courses_string = courses_string + checkbox.id.trim() + ';'
        }
    }
    console.log(courses_string)
    window.open(`${location.origin}/${year}/enade/${courses_string}`)
}

function getCourses() {
 document.querySelector('input[name="year"]:checked').value;
    var checkboxes = document.getElementsByName('check')
    for (var checks of checkboxes) {
        checks.checked = false
    }

    if (document.querySelector('input[name="year"]:checked').value == "2019") {
        document.getElementById('courses_2019').removeAttribute('hidden')
    }else {
        document.getElementById('courses_2019').setAttribute('hidden', 'hidden')
    }

    if (document.querySelector('input[name="year"]:checked').value == "2021") {
        document.getElementById('courses_2021').removeAttribute('hidden')
    }else {
        document.getElementById('courses_2021').setAttribute('hidden', 'hidden')
    }
    
    if (document.querySelector('input[name="year"]:checked').value == "2018") {
        document.getElementById('courses_2018').removeAttribute('hidden')
    }else {
        document.getElementById('courses_2018').setAttribute('hidden', 'hidden')
    }
}