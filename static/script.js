function myfunction() {
    year = document.getElementById('year').value
    courses = document.getElementById('courses').value
    window.open(`${location.origin}/${year}/enade/${courses}`)
}