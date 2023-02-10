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

