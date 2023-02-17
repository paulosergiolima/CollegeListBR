function myfunction() {    

    var checkboxes = document.getElementsByName('check')
    var states = document.getElementsByName('check_states')
    var categories = document.getElementsByName('categories')
    var courses_string = ''
    var states_string = ''
    var adm_string = ''
    for (var checkbox of checkboxes) {
        if (checkbox.checked == true) {
            courses_string = courses_string + checkbox.id.trim() + ';'
        }
    }
    for (var state of states) {
        if (state.checked == true) {
            states_string = states_string + state.id.trim() + ';'
        }
    }
    for (var adm of categories) {
        if (adm.checked == true) {
            adm_string = adm_string + adm.id.trim() + ';'
        }
    }
    console.log(courses_string)
    window.open(`${location.origin}/2021/enade/${courses_string}/${states_string}/${adm_string}`)
}

