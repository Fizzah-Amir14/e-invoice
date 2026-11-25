from playwright.sync_api import sync_playwright


def test_html_renders_to_pdf(tmp_path):
    html = "<h1>Rechnung Nr. 0001</h1><p>Gesamtbetrag: 1.234,56 €</p>"
    out = tmp_path / "test.pdf"

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        page = browser.new_page()
        page.set_content(html)
        page.pdf(path=str(out), format="A4")
        browser.close()

    assert out.exists()
    assert out.read_bytes().startswith(b"%PDF")