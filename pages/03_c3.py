import pandas as pd
from ipyvizzu import Config, Data, Style
from ipyvizzustory import Story, Slide, Step

d_types = {
    "CASO": str,
    "CODIGO": str,
    "P": str,
    "HC": str,
    "DERIVA": str,
    "Estudio": str,
    "Resultado": str,
    "GRUPO": str,
    "ETNIA": str,
    "EDAD": str,
    "CM": str,
    "RECIDIVA": str,
    "SINCRO": str,
    "DX1": str,
    "DX2": str,
    "HISTO1": str,
    "HISTO2": str,
    "GRADO1": str,
    "GRADO2": str,
    "RE1": str,
    "RE2": str,
    "RP1": str,
    "RP2": str,
    "HER21": str,
    "HER22": str,
    "HISTFAM ": str,
    "CONSANGU": str,
    "GANGLIOS1": str,
    "GANGLIOS2": str,
    "Region": str,
    "Region-corregida": str,
    "Region-1": str,
    "Region-2": str,
    "nombre-genes": str,
    "input_clinvar": str,
    "gen-clinvar": str,
    "Gene": str,
    "ID": str,
    "Accession": str,
    "Variation Name": str,
    "gene_name_variant_region": str,
    "Germline Classification": str,
    "Links": str,
}
df = pd.read_csv("etl_cenagen1.csv", dtype=d_types)
data = Data()
data.add_df(df)

story = Story(data)
story.set_size(1200, 600)
story.set_feature("tooltip", True)

story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": "count()",
                    "y": {
                        "set": ["nombre-genes", "DERIVA"],
                        "range": {"min": "auto", "max": "auto"},
                    },
                    "color": "nombre-genes",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#03ae71 #f4941b #f4c204 #d49664 #f25456 #9e67ab #bca604 #846e1c #fc763c #b462ac #f492fc #bc4a94 #9c7ef4 #9c52b4 #6ca2fc #5c6ebc #7c868c #ac968c #4c7450 #ac7a4c #7cae54 #4c7450 #9c1a6c #ac3e94 #b41204",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": "count()",
                    "y": {
                        "set": ["Germline Classification", "DERIVA"],
                        "range": {"min": "auto", "max": "auto"},
                    },
                    "color": "Germline Classification",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)

story.play()