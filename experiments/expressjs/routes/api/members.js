const express = require('express');
const router = express.Router();
const members = require('../../Members');
const uuid = require('uuid');

// This route gets all members.
router.get('/', (req, res) => res.json(members));

// Get a single member
router.get('/:id', (req, res) => {
    const found = members.some(member => member.id === parseInt(req.params.id));
    if (found) {
        res.json(members.filter(member => member.id === parseInt(req.params.id)));
    } else {
        res.status(400).json({ msg: `Member not found for id: ${req.params.id}` });
    }
});

// Create a member
router.post('/', (req, res) => {
    const newMember = {
        id: uuid.v4(),
        name: req.body.name,
        email: req.body.email,
        status: 'active'
    }
    if (!newMember.name || !newMember.email) {
        return res.status(400).json({ msg: 'Name and email are required fields' });
    }

    members.push(newMember);

    res.json(members);
    // Use the below if you're going to use this with a template and not as an API
    // res.redirect('/');
});

// Update Member
router.put('/:id', (req, res) => {
    const found = members.some(member => member.id === parseInt(req.params.id));

    if (found) {
        const updMember = req.body;
        members.forEach(member => {
            if (member.id === parseInt(req.params.id)) {
                member.name = updMember.name ? updMember.name : member.name;
                member.email = updMember.email ? updMember.email : member.email;

                res.json({ msg: 'member updated', member: member });
            }
        });
    } else {
        res.status(400).json({ msg: `Member not found for id: ${req.params.id}` });
    }
});

// Delete a member
router.delete('/:id', (req, res) => {
    const found = members.some(member => member.id === parseInt(req.params.id));

    if (found) {
        res.json({
            msg: 'Member deleted',
            members: members.filter(member => member.id !== parseInt(req.params.id))
        });
    } else {
        res.status(400).json({ msg: `Member not found for id: ${req.params.id}` });
    }
})

module.exports = router;