# Interactive Tools Patterns

## Multi-Step Survey

React pattern for surveys with conditional logic and progress tracking.

```jsx
import { useState } from 'react';

const Survey = () => {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState({});

  const questions = [
    {
      id: 'purpose',
      type: 'intro',
      content: {
        title: 'Before we begin',
        description: 'This survey takes about 5 minutes. Your responses help us [specific purpose]. All answers are [confidentiality statement].',
      }
    },
    {
      id: 'q1',
      type: 'single',
      question: '[Question text]',
      options: ['Option A', 'Option B', 'Option C'],
      // Optional: conditional next
      nextIf: { 'Option A': 'q2a', 'Option B': 'q2b', default: 'q2' }
    },
    // More questions...
    {
      id: 'complete',
      type: 'outro',
      content: {
        title: 'Thank you',
        description: 'Your input matters. Here\'s what happens next: [concrete next step]',
        // Optional: show something useful
        insight: (answers) => `Based on your responses, you might find [X] helpful.`
      }
    }
  ];

  const progress = ((step + 1) / questions.length) * 100;

  return (
    <div className="min-h-screen bg-stone-50 p-6">
      {/* Progress bar */}
      <div className="max-w-xl mx-auto mb-8">
        <div className="h-1 bg-stone-200 rounded-full">
          <div
            className="h-1 bg-stone-800 rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>
        <p className="text-sm text-stone-500 mt-2">
          {step + 1} of {questions.length}
        </p>
      </div>

      {/* Question content */}
      <div className="max-w-xl mx-auto">
        {/* Render based on question type */}
      </div>
    </div>
  );
};
```

### Question Types

**Single choice:**
```jsx
<div className="space-y-3">
  {options.map((option, i) => (
    <button
      key={i}
      onClick={() => handleAnswer(question.id, option)}
      className={`w-full text-left p-4 border rounded-lg transition-colors
        ${selected === option ? 'border-stone-800 bg-stone-100' : 'border-stone-200 hover:border-stone-400'}`}
    >
      {option}
    </button>
  ))}
</div>
```

**Multiple choice:**
```jsx
<div className="space-y-3">
  {options.map((option, i) => (
    <label key={i} className="flex items-center gap-3 p-4 border rounded-lg cursor-pointer hover:border-stone-400">
      <input
        type="checkbox"
        checked={selected.includes(option)}
        onChange={() => toggleOption(option)}
        className="w-5 h-5"
      />
      <span>{option}</span>
    </label>
  ))}
</div>
```

**Free text:**
```jsx
<textarea
  value={answers[question.id] || ''}
  onChange={(e) => handleAnswer(question.id, e.target.value)}
  placeholder="Share your thoughts..."
  className="w-full p-4 border border-stone-200 rounded-lg min-h-[150px] focus:outline-none focus:border-stone-400"
/>
```

**Scale/Rating:**
```jsx
<div className="flex justify-between gap-2">
  {[1, 2, 3, 4, 5].map((n) => (
    <button
      key={n}
      onClick={() => handleAnswer(question.id, n)}
      className={`w-12 h-12 rounded-full border-2 transition-colors
        ${selected === n ? 'border-stone-800 bg-stone-800 text-white' : 'border-stone-300 hover:border-stone-500'}`}
    >
      {n}
    </button>
  ))}
</div>
<div className="flex justify-between text-sm text-stone-500 mt-2">
  <span>Strongly disagree</span>
  <span>Strongly agree</span>
</div>
```

## Quiz with Scoring

For assessments, self-discovery tools, engagement.

```jsx
const Quiz = () => {
  const [currentQ, setCurrentQ] = useState(0);
  const [scores, setScores] = useState({});
  const [showResult, setShowResult] = useState(false);

  const questions = [
    {
      question: '[Question]',
      options: [
        { text: 'Option A', scores: { typeA: 2, typeB: 0 } },
        { text: 'Option B', scores: { typeA: 0, typeB: 2 } },
        { text: 'Option C', scores: { typeA: 1, typeB: 1 } },
      ]
    },
    // More questions...
  ];

  const results = {
    typeA: {
      title: 'You are a [Type A]',
      description: '[What this means]',
      resources: ['Resource 1', 'Resource 2']
    },
    typeB: {
      title: 'You are a [Type B]',
      description: '[What this means]',
      resources: ['Resource 1', 'Resource 2']
    }
  };

  const handleAnswer = (option) => {
    const newScores = { ...scores };
    Object.entries(option.scores).forEach(([type, points]) => {
      newScores[type] = (newScores[type] || 0) + points;
    });
    setScores(newScores);

    if (currentQ < questions.length - 1) {
      setCurrentQ(currentQ + 1);
    } else {
      setShowResult(true);
    }
  };

  const getResult = () => {
    const topType = Object.entries(scores).sort((a, b) => b[1] - a[1])[0][0];
    return results[topType];
  };

  // Render quiz or result...
};
```

## Directory with Search/Filter

For member directories, resource libraries, partner lists.

```jsx
const Directory = () => {
  const [search, setSearch] = useState('');
  const [filters, setFilters] = useState({});

  const entries = [
    {
      id: 1,
      name: '[Name]',
      type: '[Category]',
      location: '[Location]',
      tags: ['tag1', 'tag2'],
      description: '[Brief description]',
      contact: '[How to reach]'
    },
    // More entries...
  ];

  const filterOptions = {
    type: ['Category A', 'Category B', 'Category C'],
    location: ['London', 'Manchester', 'Birmingham', 'Online']
  };

  const filtered = entries.filter(entry => {
    // Search match
    const searchMatch = !search ||
      entry.name.toLowerCase().includes(search.toLowerCase()) ||
      entry.description.toLowerCase().includes(search.toLowerCase());

    // Filter matches
    const filterMatch = Object.entries(filters).every(([key, value]) =>
      !value || entry[key] === value
    );

    return searchMatch && filterMatch;
  });

  return (
    <div className="max-w-4xl mx-auto p-6">
      {/* Search */}
      <div className="mb-6">
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Search..."
          className="w-full p-4 border border-stone-200 rounded-lg"
        />
      </div>

      {/* Filters */}
      <div className="flex gap-4 mb-8">
        {Object.entries(filterOptions).map(([key, options]) => (
          <select
            key={key}
            value={filters[key] || ''}
            onChange={(e) => setFilters({...filters, [key]: e.target.value})}
            className="p-2 border border-stone-200 rounded"
          >
            <option value="">All {key}s</option>
            {options.map(opt => (
              <option key={opt} value={opt}>{opt}</option>
            ))}
          </select>
        ))}
      </div>

      {/* Results */}
      <div className="space-y-4">
        {filtered.map(entry => (
          <div key={entry.id} className="p-6 border border-stone-200 rounded-lg">
            <h3 className="font-medium text-lg">{entry.name}</h3>
            <p className="text-stone-600 text-sm mb-2">{entry.type} - {entry.location}</p>
            <p className="text-stone-700">{entry.description}</p>
            <div className="flex gap-2 mt-3">
              {entry.tags.map(tag => (
                <span key={tag} className="text-xs bg-stone-100 px-2 py-1 rounded">
                  {tag}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Add yourself prompt */}
      <div className="mt-12 p-6 bg-stone-100 rounded-lg text-center">
        <p className="text-stone-600 mb-4">Should you be listed here?</p>
        <button className="bg-stone-800 text-white px-6 py-2 rounded">
          Add your entry
        </button>
      </div>
    </div>
  );
};
```

## Sign-up Form (HTML/Tailwind)

For simple email capture, interest registration.

```html
<form class="max-w-md mx-auto" action="[endpoint]" method="POST">
  <div class="mb-4">
    <label for="email" class="block text-sm font-medium mb-1">Email</label>
    <input
      type="email"
      id="email"
      name="email"
      required
      class="w-full p-3 border border-stone-300 rounded focus:outline-none focus:border-stone-500"
      placeholder="you@example.com"
    />
  </div>

  <div class="mb-4">
    <label for="name" class="block text-sm font-medium mb-1">Name (optional)</label>
    <input
      type="text"
      id="name"
      name="name"
      class="w-full p-3 border border-stone-300 rounded focus:outline-none focus:border-stone-500"
    />
  </div>

  <!-- Optional: What brings you here -->
  <div class="mb-6">
    <label class="block text-sm font-medium mb-2">What brings you here?</label>
    <div class="space-y-2">
      <label class="flex items-center gap-2">
        <input type="checkbox" name="interest[]" value="stay-informed" class="w-4 h-4" />
        <span>Stay informed</span>
      </label>
      <label class="flex items-center gap-2">
        <input type="checkbox" name="interest[]" value="get-involved" class="w-4 h-4" />
        <span>Get involved</span>
      </label>
      <label class="flex items-center gap-2">
        <input type="checkbox" name="interest[]" value="support" class="w-4 h-4" />
        <span>Offer support</span>
      </label>
    </div>
  </div>

  <button
    type="submit"
    class="w-full bg-stone-800 text-white py-3 rounded hover:bg-stone-700 transition-colors"
  >
    Join us
  </button>

  <p class="text-xs text-stone-500 mt-4 text-center">
    [What happens with their data - be specific and honest]
  </p>
</form>
```

## Competition/Giveaway Entry

```jsx
const Competition = () => {
  const [step, setStep] = useState('entry'); // entry | confirm | success
  const [entry, setEntry] = useState({ email: '', name: '', answer: '' });

  return (
    <div className="max-w-lg mx-auto p-6">
      {step === 'entry' && (
        <form onSubmit={(e) => { e.preventDefault(); setStep('confirm'); }}>
          <h2 className="font-serif text-2xl mb-4">[Competition title]</h2>
          <p className="text-stone-600 mb-6">[What you could win]</p>

          {/* Entry fields */}
          <input
            type="email"
            required
            value={entry.email}
            onChange={(e) => setEntry({...entry, email: e.target.value})}
            placeholder="Your email"
            className="w-full p-3 border border-stone-300 rounded mb-4"
          />

          <input
            type="text"
            required
            value={entry.name}
            onChange={(e) => setEntry({...entry, name: e.target.value})}
            placeholder="Your name"
            className="w-full p-3 border border-stone-300 rounded mb-4"
          />

          {/* Optional: skill-based entry */}
          <textarea
            value={entry.answer}
            onChange={(e) => setEntry({...entry, answer: e.target.value})}
            placeholder="[Optional creative prompt]"
            className="w-full p-3 border border-stone-300 rounded mb-6 min-h-[100px]"
          />

          <button type="submit" className="w-full bg-stone-800 text-white py-3 rounded">
            Enter
          </button>

          <p className="text-xs text-stone-500 mt-4">
            [Clear terms: draw date, how winner contacted, what happens with data]
          </p>
        </form>
      )}

      {step === 'confirm' && (
        <div className="text-center">
          <h2 className="font-serif text-2xl mb-4">Confirm your entry</h2>
          <p className="text-stone-600 mb-6">
            We'll email {entry.email} if you win. Make sure that's right!
          </p>
          <div className="flex gap-4 justify-center">
            <button onClick={() => setStep('entry')} className="px-6 py-2 border border-stone-300 rounded">
              Go back
            </button>
            <button onClick={() => setStep('success')} className="px-6 py-2 bg-stone-800 text-white rounded">
              Confirm
            </button>
          </div>
        </div>
      )}

      {step === 'success' && (
        <div className="text-center">
          <h2 className="font-serif text-2xl mb-4">You're in!</h2>
          <p className="text-stone-600 mb-6">
            [What happens next - when draw happens, how they'll know]
          </p>
          {/* Optional: share for extra entries */}
          <p className="text-sm text-stone-500">
            [Invite to share, follow, etc. - but don't make it manipulative]
          </p>
        </div>
      )}
    </div>
  );
};
```

---
