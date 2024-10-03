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
story.set_size(640, 480)
story.set_feature("tooltip", True)

story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": ["nombre-genes", "RECIDIVA"],
                    "y": {"set": "count()", "range": {"min": "auto", "max": "110%"}},
                    "color": "RECIDIVA",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
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
                    "x": ["ETNIA", "nombre-genes"],
                    "y": {"set": "count()", "range": {"min": "auto", "max": "110%"}},
                    "color": "ETNIA",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
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
                        "set": ["CM", "nombre-genes"],
                        "range": {"min": "auto", "max": "auto"},
                    },
                    "color": "CM",
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
                            "colorPalette": "#eb0000 #fd7c4b #cc9577 #fda276 #d5895b #dc9376 #a46850 #fd723c #e97c5e #b3654e #b75121 #966443 #d15948 #fd6a4a #fe9f8a #bb5b58 #fb786c #fc5a54 #fd8047 #fe4e49 #ff8d69 #dab18f #e9908f #9e8171 #99746b",
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
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": ["EDAD", "count()"],
                    "y": {
                        "set": "nombre-genes",
                        "range": {"min": "-50%", "max": "auto"},
                    },
                    "color": "EDAD",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "stretch",
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
                            "rectangleSpacing": 0,
                            "circleMinRadius": 0.015,
                            "borderOpacity": 0,
                            "colorPalette": "#3394b6 #5ab4cb #4199b9 #599f9c #bf7caf #b6918b #8785a9 #76b4ce #8f8dba #6b789e #6b5c78 #757284 #8ea5be #8498aa #778393 #b897a4 #64ad9f #977675 #65dbd5",
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
                    "x": ["ID", "count()"],
                    "y": {
                        "set": "nombre-genes",
                        "range": {"min": "auto", "max": "auto"},
                    },
                    "color": "ID",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": True,
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
                            "colorPalette": "#e5b96c #d0ae5e #f1cc6a #dac7a8 #d79984 #ff982c #d0f58e #bdbce4 #66bcce #80a4df #ceab80 #ff6b87 #e6a273 #e9c994 #cc9065 #d6a258 #e8ac97 #f5b887 #f8cf93 #f5b9b0 #ff91a6",
                        },
                    }
                }
            ),
        )
    )
)

story.play()