FILES=("analyze.py" "run_analysis.sh" "upload_to_github.sh" "output.txt" "log.txt" "environment.yml" "README.md")
git init
git add "${FILES[@]}"
git commit -m "Add analysis scripts and results"
git remote add origin https://github.com/linryu/wine_analysis_project.git
git push -u origin master