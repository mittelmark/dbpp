-- Pandoc filter to process code blocks with class "kroki" containing
-- Diagram code dfor the kroki webservice
-- see https://kroki.io and https://niolesk.top

local function compress(text)
    -- print(base64.urlsafe_b64encode(zlib.compress("test".encode())).decode("ascii"))'
    local command ="python3 -c 'import base64, zlib; print(base64.urlsafe_b64encode(zlib.compress(\"\"\"" .. text .. "\"\"\".encode(), 9)).decode(\"ascii\"),end=\"\")'"
    local handle = io.popen(command)
    local result = handle:read("*a")
    handle:close()
    return(result)
end

function CodeBlock(block)
    if block.classes[1] == "py" then
        w = io.open("temp.py","w")
        w:write(block.text)
        w:close()
        local command ="python3 temp.py"
        local handle = io.popen(command)
        local result = handle:read("*a")
        handle:close()
        local echo = block.attributes.echo or "true"
        if (echo == "true") then
            return {block, pandoc.CodeBlock(result) }
        else
            return {pandoc.CodeBlock(result)}
        end
    end
end
