box.cfg{
    listen = 3301,
    wal_mode = 'write',
    log_level = 5,
    read_only = false,
}
box.once('init', function()
    local space = box.schema.space.create('tester')

    space:create_index('primary', {
        type = 'tree',
        parts = {1, 'unsigned'}
    })
end)