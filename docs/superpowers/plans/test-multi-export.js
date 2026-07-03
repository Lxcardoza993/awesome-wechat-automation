export const meta = {
  name: "test-multi-export",
  description: "Test multiple exports.",
  phases: [{ title: "Test", detail: "Run a no-op agent" }]
};

phase("Test");
const result = await agent("Return hello", { label: "test", schema: { type: "object", properties: { value: { type: "string" } }, required: ["value"] } });
log(result.value);

export const resultObj = { value: result.value };
