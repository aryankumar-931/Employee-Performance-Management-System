def generate_feedback(
    attendance,
    task_completion,
    quality_score,
    manager_feedback
):

    strengths = []
    improvements = []
    recommendations = []

    # Attendance
    if attendance >= 80:
        strengths.append("Excellent attendance record")
    else:
        improvements.append("Attendance needs improvement")
        recommendations.append("Improve punctuality and attendance consistency")

    # Task Completion
    if task_completion >= 80:
        strengths.append("Strong task completion rate")
    else:
        improvements.append("Task completion is below expectation")
        recommendations.append("Improve task planning and execution")

    # Quality Score
    if quality_score >= 80:
        strengths.append("High quality of work")
    else:
        improvements.append("Work quality can be improved")
        recommendations.append("Focus on accuracy and quality standards")

    # Manager Feedback
    if manager_feedback >= 80:
        strengths.append("Positive manager feedback")
    else:
        improvements.append("Manager feedback indicates improvement areas")
        recommendations.append("Regular review meetings with manager")

    return strengths, improvements, recommendations