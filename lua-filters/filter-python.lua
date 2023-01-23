-- Pandoc filter to process code blocks with class "py" 
-- containing Python code
-- the following chunk attributes are supported
--    - echo - should the source code been, showm default=true
--    - eval - should the Python code be evaluated, default=false

function CodeBlock(block)
    if block.classes[1] == "py" then
        local echo = block.attributes.echo or "true"
        local eval = block.attributes.eval or "false"
        local result = ""
        if (eval == "true") then
            w = io.open("temp.py","w")
            w:write(block.text)
            w:close()
            local command ="python3 temp.py"
            local handle = io.popen(command)
            result = handle:read("*a")
            handle:close()
        end
        if (echo == "true") then
            if (result ~= "") then
                return {block, pandoc.CodeBlock(result) }
            else
                return {block}
            end
        else
            if (result ~= "") then
                return {pandoc.CodeBlock(result)}
            else
                return {}
            end
        end
    end
end
