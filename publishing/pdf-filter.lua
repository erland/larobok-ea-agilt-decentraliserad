-- Gemensam rubrikformatering för EPUB och PDF.
-- H1 av typen "Kapitel N: Titel" delas visuellt i två rader.
-- Inledningen behålls som egen H1/top-level-post.

local function inline_latex_from_markdown(text)
  local doc = pandoc.read(text, "markdown")
  local blocks = doc.blocks
  if #blocks == 0 then
    return text
  end
  local para = blocks[1]
  local pd = pandoc.Pandoc({pandoc.Para(para.content)})
  local latex = pandoc.write(pd, "latex")
  return latex:gsub("%s+$", "")
end

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match("^Kapitel%s+(%d+):%s*(.+)%s*$")

  if FORMAT:match("latex") then
    if number then
      local title_tex = inline_latex_from_markdown(title)
      return pandoc.RawBlock(
        "latex",
        "\\bookchapter{" .. number .. "}{" .. title_tex .. "}"
      )
    elseif text == "Inledning" then
      return pandoc.RawBlock(
        "latex",
        "\\bookintro{Inledning}"
      )
    end
    return nil
  end

  if FORMAT:match("epub") or FORMAT:match("html") then
    if number then
      local title_doc = pandoc.read(title, "markdown")
      local title_inlines = title_doc.blocks[1].content

      local chapter_number = pandoc.Span(
        { pandoc.Str("Kapitel"), pandoc.Space(), pandoc.Str(number) },
        pandoc.Attr("", {"chapter-number"})
      )
      local chapter_title = pandoc.Span(
        title_inlines,
        pandoc.Attr("", {"chapter-title"})
      )

      el.content = {
        chapter_number,
        pandoc.LineBreak(),
        chapter_title
      }
      el.classes:insert("chapter-heading")
      return el
    end
  end

  return nil
end
