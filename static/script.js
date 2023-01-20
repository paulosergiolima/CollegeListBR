function myfunction() {
    year = document.getElementById('year').value
    courses = document.getElementById('courses').value
    window.open(`http://127.0.0.1:5000/${year}/enade/${courses}`)
}