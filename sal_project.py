from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd

# ====================== главная страница ============================
# параметры главной страницы
# https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="Project_salary_analysis",
    page_icon="🧊",
)
# ----------- функции -------------------------------------

# функция для загрузки картинки с диска
# кэшируем, иначе каждый раз будет загружаться заново
@st.cache_data
def load_image(image_path):
    image = Image.open(image_path)
    # обрезка до нужного размера с сохранением пропорций
    MAX_SIZE = (2000,600)
    image.thumbnail(MAX_SIZE)
    return image

# ------------- загрузка картинки для страницы и модели ---------

# путь до картинки
image_path = Path.cwd() / 'real_sal_img.png'
image = load_image(image_path)
image_path2 = Path.cwd() / 'build_infl.png'
image2 = load_image(image_path2)
image_path3 = Path.cwd() / 'educ_infl.png'
image3 = load_image(image_path3)
image_path4 = Path.cwd() / 'infl.png'
image4 = load_image(image_path4)
image_path5 = Path.cwd() / 'build_sal.png'
image5 = load_image(image_path5)
image_path6 = Path.cwd() / 'educ_sal.png'
image6 = load_image(image_path6)
image_path7 = Path.cwd() / 'med_sal.png'
image7 = load_image(image_path7)
image_path8 = Path.cwd() / 'med_infl.png'
image8 = load_image(image_path8)
# ---------- отрисовка текста и картинки ------------------------
st.write(
    """
    # Анализ зарплат в России за 2000-2023гг.:
    в строительстве, образовании, здравохранении
    """
)

# отрисовка картинки на странице
st.write("#### Графики изменения реальных и номинальных среднемесячных зп по 3 видам экономической деятельности за 2000-2023гг. с учетом инфляции")
st.image(image)
st.image(image5)
st.image(image6)
st.image(image7)

st.write(
    """
    Выводы:
- Если смотреть на графики роста зп по годам и видам деятельности, то видим,что, начиная с 2019 г, уровень реальной зп в медицине обогнал значения зп в образовании и строительстве, это было связано с пандемией ковида (доплатами за работу в ковидных стационарах) в это время и закрытием строительных предприятий на lockdown. После завершения пандемии строительство возобновилось и уровень зп в строительстве снова превышает уровень зп в медицине и в образовании.
- 3 графика, на которых визуализированы по годам среднемесячные номинальные и реальные зп по 3 видам деятельности подтверждают,что рельные зп работников меньше, чем номинальные зп, потому что индексирование зп не покрывает уровень инфляции. Особенно это видно в 2008-2009г, 2014-2015г, 2022г, что связано с геополитическими событиями в нашей стране.
 """)
st.write("#### График изменения уровня инфляции за 2000-2023гг.")
st.image(image4)
st.write(
    """
    Выводы:
- самая маленькая инфляция была в 2017г - 2,52
- самая большая инфляция была в 2000г - 20,20 - это отголоски дефолта рубля в 1998г.
- также видим зависимость повышения уровня инфляции в 2008г, 2014-2015г, 2022г, связанную с геополитической ситуацией нашей страны.
    """)
st.write("#### Графики сравнения значений инфляции, индексов повышения зп по 3 видам деятельности, и индексы фактического повышения рельной зп с учетом инфляции за 2000-2023гг.")
st.image(image2)
st.write(
    """
    Выводы:
- в строительстве в начале 2000-х гг. индексирование зп как рельных, так и номинальных превосходило уровень инфляции, было больше 20%. Резкое снижение реальных зп произошло в 2004, 2009, 2014-2015, 2020-2021, 2022 гг. - это было связано с геополитической ситуацией в стране и в мире, а также пандемия ковида повлияла в 2020-2021 гг. Инфляция съедала повышение зп даже в минус.
- также фактическое повышение реальной зп превышало уровень инфляции с 2016-2019гг, но не больше 20% как в начале 2000-х гг.
 """)
st.image(image3)
st.write(
    """
    Выводы:
- в образовании  в начале 2000-х гг. индексирование зп как рельных, так и номинальных превосходило уровень инфляции, было больше 20%, доходило до 50%. Резкое снижение реальных зп произошло в 2003, 2010,2014-2015, 2020-2022 гг. - скорее всего это также было связано с геополитической ситуацией в стране.Уровень инфляции значительно превысил реальные и номинальные зп.
- также фактическое повышение реальной зп превышало уровень инфляции с 2004-2008, 2011-2013, 2017-2019гг, доходило до 20% повышение.
 """)
st.image(image8)
st.write(
    """
    Вывод:
- в здравохранении  до 2003г, с 2004-2008, 2011-2013, с 2016-2020 гг. индексирование зп как рельных, так и номинальных превосходило уровень инфляции. Ниже уровня инфляции повышение зп в здравохранении было в 2003, 2008-2011,2014-2016, 2021-2023 гг.
 """)

# считываем данные с моего гугл диска
df_sal_ind = st.cache_data(pd.read_csv)('https://drive.google.com/u/0/uc?id=1N32qkJvC_QkSKiOQV1owmtkwh6KQhvOM&export=download')
st.write("#### Данные по зп, инфляции и индексированию зп по 3 видам экономической деятельности:")
st.write(
    """
    Столбцы и их значения:
- 'year' - год.
- 'Всего' - уровень инфляции общий за год.
- 'building' - номинальная зп в строительстве.
- 'real_sal_build' - реальная зп с учетом инфляции в строительстве.
- 'ind_b' - индекс повышения номин. зп по сравнению с предыд. годом в строительстве.
- 'ind_b_infl'- индекс повышения номин. зп по сравнению с предыд. годом с учетом инфляции в этом году в строительстве.
- 'ind_rb'-  индекс повышения реальной зп по сравнению с предыд. годом в строительстве.
- 'ind_rb_infl'-  индекс повышения реальной зп по сравнению с предыд. годом с учетом инфляции в этом году в строительстве.
- 'education'- номинальная зп в образовании.
- 'real_sal_educ'- реальная зп с учетом инфляции в образовании.
- 'ind_e'- индекс повышения номин. зп по сравнению с предыд. годом в образовании.
- 'ind_e_infl'- индекс повышения номин. зп по сравнению с предыд. годом с учетом инфляции в этом году  в образовании.
- 'ind_re'- индекс повышения реальной зп по сравнению с предыд. годом в образовании.
- 'ind_re_infl'-  индекс повышения реальной зп по сравнению с предыд. годом с учетом инфляции в этом году в образовании.
- 'medicine'- номинальная зп в здавохранении.
- 'real_sal_med'- реальная зп с учетом инфляции в здавохранении.
- 'ind_m'- индекс повышения номин. зп по сравнению с предыд. годом в здравохранении.
- 'ind_m_infl'- индекс повышения номин. зп по сравнению с предыд. годом с учетом инфляции в этом году в здравохранении.
- 'ind_rm'- индекс повышения реальной зп по сравнению с предыд. годом в здравохранении.
- 'ind_rm_infl'-  индекс повышения реальной зп по сравнению с предыд. годом с учетом инфляции в этом году в здравохранении.
"""
)
st.dataframe(df_sal_ind.style.format('{:.2f}'))
st.write(
    """
    Выводы:
- если смотреть по таблице, то конечно номинальная и реальная зп отличаются по всем видам деятельности, потому что на нее влияет уровень инфляции, реальная зп меньше, чем номинальная зп.
- если сравнивать по процентам индексирования зп, то например, в 2001г по сравнению с 2000г в строительстве номинальная зп увеличилась на 46,17%, реальная зп увеличилась на 49,14%, но с учетом инфляции в 2001г-18,58% фактическое увеличение номинальной зп составило- 27,59%, а реальной зп - 30,56%
    """)
