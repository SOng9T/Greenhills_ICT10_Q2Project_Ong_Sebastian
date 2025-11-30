from pyscript import document, display
import math

# Using TUPLE for subjects and units (immutable) the following comments are utilized from the study notes, copied a bit of them there and from our exercises! 
subjects = ("Science", "Math", "English", "Chinese", "ICT", "PE")
units = (3, 3, 3, 3, 3, 3)

# Using LIST to store grades (mutable)
grades_list = []

# Using DICTIONARY for club information (was absent from this lecture, saw a w3schools and reddit article about it)
clubs_dict = {
    'robotics': {
        'name': "Robotics Club | 机器人俱乐部",
        'description': "Design, build, and program robots for competitions. | 设计、构建和编程机器人参加比赛",
        'schedule': "Every Tuesday 3:45-5:30 PM | 每周二下午3:45-5:30",
        'location': "Computer Lab | 计算机实验室",
        'advisor': "Professor Zhang | 张教授",
        'members': 18
    },
    'ai': {
        'name': "AI & Machine Learning Club | 人工智能与机器学习俱乐部", 
        'description': "Explore AI applications and machine learning models. | 探索人工智能应用和机器学习模型",
        'schedule': "Every Wednesday 4:00-6:00 PM | 每周三下午4:00-6:00",
        'location': "AI Lab | 人工智能实验室", 
        'advisor': "Dr. Li | 李博士",
        'members': 32
    },
    'engineering': {
        'name': "Traditional Engineering Club | 传统工程俱乐部",
        'description': "Study ancient Chinese engineering techniques. | 研究中国古代工程技术",
        'schedule': "Every Thursday 3:30-5:00 PM | 每周四下午3:30-5:00", 
        'location': "Engineering Hall | 工程大厅",
        'advisor': "Professor Chen | 陈教授",
        'members': 28
    }
}

def calculate_gwa(e=None):
    """Calculate General Weighted Average using PyScript"""
    name = document.getElementById("name").value
    #ms. pasco gave a small lesson on this code, helped a lot
    if not name:
        # Instead of generic display, modify the results card to show an error
        results_div = document.getElementById("results")
        results_div.classList.remove("hidden")
        document.getElementById("studentInfo").innerHTML = "<p class='text-danger'><strong>Error:</strong> Please enter your name!</p>"
        document.getElementById("gradeTable").innerHTML = ""
        document.getElementById("gwa").textContent = "N/A"
        return
    
    # Clear previous grades
    grades_list.clear()
    
    # Get grades from input fields
    total_weighted_grade = 0
    total_units = 0
    
    for i, subject in enumerate(subjects):
        grade_input = document.getElementById(f"grade_{subject}")
        # Added check for missing input element, although unlikely in this setup
        if not grade_input:
            display(f"Critical Error: Missing input field for {subject}", target="results", append=False)
            return

        if grade_input.value:
            try:
                grade = float(grade_input.value)
                if 0 <= grade <= 100:
                    grades_list.append(grade)
                    total_weighted_grade += grade * units[i]
                    total_units += units[i]
                else:
                    results_div = document.getElementById("results")
                    results_div.classList.remove("hidden")
                    document.getElementById("studentInfo").innerHTML = f"<p class='text-danger'><strong>Error:</strong> Please enter valid grade for {subject} (0-100)</p>"
                    document.getElementById("gradeTable").innerHTML = ""
                    document.getElementById("gwa").textContent = "N/A"
                    return
            except ValueError:
                results_div = document.getElementById("results")
                results_div.classList.remove("hidden")
                document.getElementById("studentInfo").innerHTML = f"<p class='text-danger'><strong>Error:</strong> Please enter a number for {subject}</p>"
                document.getElementById("gradeTable").innerHTML = ""
                document.getElementById("gwa").textContent = "N/A"
                return
        else:
            results_div = document.getElementById("results")
            results_div.classList.remove("hidden")
            document.getElementById("studentInfo").innerHTML = f"<p class='text-danger'><strong>Error:</strong> Please enter grade for {subject}</p>"
            document.getElementById("gradeTable").innerHTML = ""
            document.getElementById("gwa").textContent = "N/A"
            return
    
    # Calculate general weighted average yah
    if total_units > 0:
        gwa = total_weighted_grade / total_units
        display_results(name, gwa)
    else:
        results_div = document.getElementById("results")
        results_div.classList.remove("hidden")
        document.getElementById("studentInfo").innerHTML = "<p class='text-danger'><strong>Error:</strong> Total units must be greater than zero.</p>"
        document.getElementById("gradeTable").innerHTML = ""
        document.getElementById("gwa").textContent = "N/A"


def display_results(name, gwa):
    """Display the calculation results"""
    results_div = document.getElementById("results")
    results_div.classList.remove("hidden")
    
    # Student info
    student_info = f"<p><strong>Name | 姓名:</strong> {name}</p>"
    document.getElementById("studentInfo").innerHTML = student_info
    
    # Grade table
    grade_table = ""
    for i, subject in enumerate(subjects):
        grade_table += f"""
            <tr>
                <td>{subject}</td>
                <td>{units[i]}</td>
                <td>{grades_list[i]:.2f}</td>
            </tr>
        """
    document.getElementById("gradeTable").innerHTML = grade_table
    
    # GWA result
    document.getElementById("gwa").textContent = f"{gwa:.2f}"

def show_club_info(club_key):
    """Display club information using PyScript and update the active state"""
    club = clubs_dict.get(club_key)
    
    # Update active class on the list-group items
    # Since the HTML uses py-click, we can focus on displaying the content
    
    if club:
        club_info = f"""
            <div class="card">
                <div class="card-header">
                    <h3>{club['name']}</h3>
                </div>
                <div class="card-body">
                    <p><strong>Description | 描述:</strong> {club['description']}</p>
                    <p><strong>Schedule | 时间:</strong> {club['schedule']}</p>
                    <p><strong>Location | 地点:</strong> {club['location']}</p>
                    <p><strong>Advisor | 指导老师:</strong> {club['advisor']}</p>
                    <p><strong>Members | 成员:</strong> {club['members']}</p>
                    <button class="btn btn-primary mt-3">Join This Club | 加入俱乐部</button>
                </div>
            </div>
        """
        display(club_info, target="club-info-container", append=False)

def initialize_grade_inputs():
    """Initialize grade input fields when page loads"""
    grade_inputs_div = document.getElementById("gradeInputs")
    if grade_inputs_div:
        inputs_html = ""
        for subject in subjects:
            unit = units[subjects.index(subject)]
            inputs_html += f"""
                <div class="col-md-6 mb-3">
                    <label for="grade_{subject}" class="form-label">{subject} ({unit} units)</label>
                    <input type="number" class="form-control" id="grade_{subject}" min="0" max="100" required>
                </div>
            """
        grade_inputs_div.innerHTML = inputs_html

def initialize_club_info():
    """Display the first club's info (Robotics) on page load"""
    # This automatically shows the info for the 'active' club when the page loads
    show_club_info('robotics')

def main():
    """Initializes the required elements after PyScript is ready."""
    initialize_grade_inputs()
    initialize_club_info()

# Note: The 'main()' function is now called by the <py-script src="./main.py" once> tag in the HTML.
# No need for raw function calls at the end of this script.