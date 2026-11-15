#!/usr/bin/env python3
"""
trends_miner.py — Motor de Conteúdo
Busca as principais tendências de um nicho no Google Trends Brasil.
Uso: python3 trends_miner.py "nutrição"
"""

import sys
import json
import warnings
warnings.filterwarnings("ignore")

from pytrends.request import TrendReq


def buscar_tendencias(nicho: str, top_n: int = 20):
    pt = TrendReq(hl="pt-BR", tz=-180)

    # 1. Buscas relacionadas
    pt.build_payload([nicho], timeframe="today 12-m", geo="BR")
    topo = []
    crescendo = []
    try:
        relacionadas = pt.related_queries()
        if relacionadas.get(nicho):
            df_top = relacionadas[nicho].get("top")
            df_rise = relacionadas[nicho].get("rising")
            if df_top is not None:
                topo = df_top.head(top_n)[["query", "value"]].to_dict("records")
            if df_rise is not None:
                crescendo = df_rise.head(10)[["query", "value"]].to_dict("records")
    except Exception as e:
        print(f"  ⚠️  related_queries: {e}")

    # 2. Tópicos relacionados
    top_topicos = []
    try:
        topicos = pt.related_topics()
        if topicos.get(nicho):
            df_t = topicos[nicho].get("top")
            if df_t is not None and not df_t.empty:
                top_topicos = df_t.head(10)[["topic_title", "value"]].to_dict("records")
    except Exception as e:
        print(f"  ⚠️  related_topics: {e}")

    resultado = {
        "nicho": nicho,
        "periodo": "últimos 12 meses",
        "pais": "Brasil",
        "top_buscas": topo,
        "buscas_em_alta": crescendo,
        "top_topicos": top_topicos,
    }
    return resultado


def comparar_ganchos(ganchos: list, buscas: list):
    resultado = []
    for gancho in ganchos:
        palavras = set(gancho.lower().split())
        matches = []
        for busca in buscas:
            query = busca["query"].lower()
            palavras_query = set(query.split())
            intersecao = palavras & palavras_query
            if intersecao:
                matches.append({
                    "busca": busca["query"],
                    "volume": busca["value"],
                    "palavras_em_comum": list(intersecao)
                })
        resultado.append({
            "gancho": gancho,
            "matches": sorted(matches, key=lambda x: x["volume"], reverse=True)[:3],
            "score": len(matches)
        })
    return sorted(resultado, key=lambda x: x["score"], reverse=True)


if __name__ == "__main__":
    nicho = sys.argv[1] if len(sys.argv) > 1 else "nutrição"
    print(f"\n🔍 Buscando tendências para: {nicho}\n")

    dados = buscar_tendencias(nicho)

    print(f"📊 TOP BUSCAS ({len(dados['top_buscas'])} encontradas):")
    for i, b in enumerate(dados["top_buscas"][:15], 1):
        print(f"  {i:2}. {b['query']} (volume: {b['value']})")

    if dados["buscas_em_alta"]:
        print(f"\n🚀 BUSCAS EM ALTA:")
        for b in dados["buscas_em_alta"][:8]:
            v = b['value']
            label = f"+{v}%" if isinstance(v, (int, float)) and v < 5000 else "em explosão"
            print(f"  ↑ {b['query']} ({label})")
    else:
        print(f"\n🚀 BUSCAS EM ALTA: nenhuma retornada pela API")

    if dados["top_topicos"]:
        print(f"\n📌 TÓPICOS RELACIONADOS:")
        for t in dados["top_topicos"][:5]:
            print(f"  • {t['topic_title']}")
    else:
        print(f"\n📌 TÓPICOS RELACIONADOS: nenhum retornado pela API")

    # Salvar JSON
    output_file = f"/Users/marilia/motor-conteudo/trends_{nicho.replace(' ', '_')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Dados salvos em: {output_file}")
