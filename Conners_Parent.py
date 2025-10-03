import pandas as pd

##df = pd.read_csv(r"C:\Users\Mariana Muszynska\Downloads\connersquests_p_1281_.csv")

df_conners = df[df["Q-KEY"] == "CONNERS4_Pt2"] # I have a lot of questionnaires in one CSV - so this code picks up only ones that are labelled CONNERS$_Pt2
## this can be changed to whatever happens in your file

## below is a dmain map - which question belongs to which ADHD domain
parent_domain_map = {
    "Hyperactivity": [3, 14, 18, 47, 51, 60, 69, 86, 95, 108, 111],
    "Impulsivity": [9, 25, 50, 55, 75, 89, 97, 106, 109],
    "Inattention": [2, 5, 7, 10, 15, 19, 26, 32, 42, 48,
                    57, 62, 66, 71, 79, 87, 93, 102, 105,
                    107, 98],
    "EmotionalDysregulation": [4, 30, 39, 52, 65, 80, 92, 113],
    "DepressedMood": [8, 36, 54, 82, 94, 110],
    "AnxiousThoughts": [22, 46, 72, 99, 112],
    "Schoolwork": [24, 40, 56, 64, 74, 114],
    "PeerInteractions": [1, 20, 38, 63, 73, 100],
    "FamilyLife": [13, 28, 41, 53, 78, 88],
}

## the below piece of code calculates only raw scores per each domain and creates a csv with those results. 
results = []
for pid, group in df_conners.groupby("PID"):
    row = {"PID": pid}
    for domain, items in parent_domain_map.items():
        # sum the 'VALUE' column where QUESTION ID is in 'items'
        row[domain] = group.loc[group["QUESTION ID"].isin(items), "VALUE"].sum()
    results.append(row)

df_scores = pd.DataFrame(results)

# 5) Write this new domain-scores DataFrame to CSV
df_scores.to_csv("conners4_scores.csv", index=False)

print("Done! Wrote conners4_scores.csv")