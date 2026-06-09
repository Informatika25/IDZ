import os

#Добавленный отдельный блок
folder_name = "data"

# Создаем папку, если она еще не существует
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Папка '{folder_name}' успешно создана.")
    print("Внесите в нее следующие исходные файлы перед полноценным запуском:")
    print(" - Сводный_прошлый_год.xlsx")
    print(" - Осень.xlsx")
    print(" - Весна.xlsx\n")

os.chdir(folder_name)

import pandas as pd


class WorkloadLoader:
    def __init__(self):
        self.last_year = None
        self.autumn = None
        self.spring = None

    def load_file(self, path):
        try:
            df = pd.read_excel(path)

            print(f"\nФайл: {path}")
            print(f"Количество строк: {len(df)}")
            print(f"Количество столбцов: {len(df.columns)}")

            print("\nСтолбцы:")
            for column in df.columns:
                print(f"- {column}")

            return df

        except Exception as e:
            print(f"Ошибка загрузки файла {path}: {e}")
            return None

    def analyze_data(self, df, file_name):
        if df is None:
            return

        print("\n" + "=" * 50)
        print(file_name)
        print("=" * 50)

        if "Название" in df.columns:
            print("\nДисциплины:")
            print(df["Название"].dropna().unique())

        if "Группа" in df.columns:
            print("\nГруппы:")
            print(df["Группа"].dropna().unique())

        if "Вид" in df.columns:
            print("\nВиды нагрузки:")
            print(df["Вид"].dropna().unique())

        if "Нагрузка" in df.columns:
            print("\nСуммарная нагрузка:")
            print(df["Нагрузка"].sum())

        print("\nПервые 5 строк:")
        print(df.head())

    def load_all_files(self,
                       last_year_path,
                       autumn_path,
                       spring_path):

        print("Загрузка файлов")

        self.last_year = self.load_file(last_year_path)
        self.autumn = self.load_file(autumn_path)
        self.spring = self.load_file(spring_path)

        print("\nВсе файлы успешно загружены.")

    def show_information(self):
        self.analyze_data(
            self.last_year,
            "Сводный файл прошлого года"
        )

        self.analyze_data(
            self.autumn,
            "Файл текущего года - Осень"
        )

        self.analyze_data(
            self.spring,
            "Файл текущего года - Весна"
        )


def main():
    loader = WorkloadLoader()

    loader.load_all_files(
        "Сводный_прошлый_год.xlsx",
        "Осень.xlsx",
        "Весна.xlsx"
    )

    loader.show_information()


if __name__ == "__main__":
    main()