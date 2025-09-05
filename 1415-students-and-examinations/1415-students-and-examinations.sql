SELECT
    st.student_id,
    st.student_name,
    sj.subject_name,
    SUM(CASE WHEN sj.subject_name = e.subject_name THEN 1 ELSE 0 END) AS attended_exams
FROM
    Students AS st
CROSS JOIN
    Subjects AS sj
LEFT JOIN
    Examinations AS e
ON
    st.student_id = e.student_id
GROUP BY
    st.student_id, sj.subject_name
ORDER BY
    st.student_id, sj.subject_name