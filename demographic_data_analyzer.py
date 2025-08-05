import pandas as pd


def calculate_demographic_data(print_data=True):
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country",
        "salary"
    ]

    df = pd.read_csv('adult.data.csv',
                     header=None,
                     names=column_names,
                     skipinitialspace=True)

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100,
                                 1)

    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education = ~higher_education
    lower_edu_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()
    min_workers = df['hours-per-week'] == min_work_hours
    rich_min_workers = df[min_workers & (df['salary'] == '>50K')]
    rich_percentage = round(
        len(rich_min_workers) / len(df[min_workers]) * 100, 1)

    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] ==
                             '>50K']['native-country'].value_counts()
    country_percentage = (rich_country_counts / country_counts * 100).dropna()
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    top_IN_occupation = df[(df['native-country'] == 'India')
                           & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:",
              higher_edu_rich)
        print("Percentage without higher education that earn >50K:",
              lower_edu_rich)
        print("Minimum work hours per week:", min_work_hours)
        print("Percentage of rich among those who work minimum hours:",
              rich_percentage)
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print("Highest percentage of rich people in country:",
              highest_earning_country_percentage)
        print("Top occupation in India for those earning >50K:",
              top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
